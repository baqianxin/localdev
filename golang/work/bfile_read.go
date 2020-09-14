package main

import (
	"bufio"
	"bytes"
	"encoding/csv"
	"errors"
	"fmt"
	"io"
	"log"
	"os"
	"os/exec"
	"path"
	"sort"
	"strconv"
	"strings"
	"time"
)

func main() {

	var parttenData = make(map[string]string)
	// 恒丰银行
	// parttenData["15890165720"] = `用户名`
	// parttenData["peng630129"] = `密码`
	// parttenData["630129"] = `交易密码`

	// 万支付
	// parttenData["13369458910"] = `用户名`
	// parttenData["111111"] = `密码`

	// 测试账号：13910785385
	// 登录密码：147258qwe
	// 支付密码：147258
	// 登录
	parttenData["13910785385"] = `用户名`
	parttenData["147258qwe"] = `登录密码`
	parttenData["147258"] = `密码`
	searchResultFilePath := "search.list"

	var rd = make(map[string]string)
	rd["search_data_log.csv"] = path.Join(".", "data", "dump_file", "data")
	rd["search_console_log.csv"] = path.Join(".", "data", "dump_file", "console.log")
	rd["search_memory_log.csv"] = path.Join(".", "data", "dump_file", "memory.log")

	// 1.执行导出脚本
	// python fridump.py -U -s PACKAGE.NAME	 -o /tmp/scan/PACKAGE.NAME/memory --packageName PACKAGE.NAME --data /tmp/scan/PACKAGE.NAME/data --log /tmp/scan/PACKAGE.NAME/console.log --signal /tmp/scan/PACKAGE.NAME/siganl

	// 2.监听信号文件
	// go WatchSignalFile(/tmp/scan/PACKAGE.NAME/siganl)

	// 3.清理结果数据：移动导出的文件到指定路径 /tmp/scan/PACKAGE.NAME/*

	// 4.构建文本扫描脚本
	// 4.1扫描参数

	// 5.执行扫描脚本，写入CSV文件
	// csv文件列表，对应用户选择

	// 6.打包日志文件+扫描结果文件

	for k, v := range rd {
		cmdparams := "grep -ain"
		if IsDir(v) {
			cmdparams = "grep -rlin"
		}
		Run(k, v, searchResultFilePath, parttenData, cmdparams)
	}

}

// IsDir 判断所给路径是否为文件夹
func IsDir(path string) bool {
	s, err := os.Stat(path)
	if err != nil {
		return false
	}
	return s.IsDir()
}

//GetFileModTime 获取文件修改时间 返回unix时间戳
func GetFileModTime(path string) string {
	f, err := os.Open(path)
	if err != nil {
		log.Println("open file error")
		return time.Now().Format("01/02/2006 15:04:05")
	}
	defer f.Close()

	fi, err := f.Stat()
	if err != nil {
		log.Println("stat fileinfo error")
		return time.Now().Format("01/02/2006 15:04:05")
	}

	return fi.ModTime().Format("01/02/2006 15:04:05")
}

// Run 导出关键字数据
func Run(filename, filepath, searchResultFilePath string, parttenData map[string]string, params string) {
	var mpd = make(map[int][]string)
	var partten, parttenName string
	var i int = 0
	mt := GetFileModTime(filepath)
	for k, v := range parttenData {

		partten = k
		parttenName = v
		sf, _ := os.Create(searchResultFilePath)
		searchResult, _ := searchFile(partten, filepath, params)

		sf.WriteString(searchResult.String())
		sf.Close()
		file, _ := os.Open(searchResultFilePath)
		br := bufio.NewReader(file)
		var j = 0
		for {
			a, _, c := br.ReadLine()
			if c == io.EOF {
				break
			}
			if string(a) == "<nil>" {
				break
			}
			// 构造map 写入csv
			v := string(a)
			if len(a) == 0 {
				v = "未找到匹配数据"
			}

			mpd[i] = []string{strconv.Itoa(i + 1), parttenName, partten, v, mt}
			i++
			j++
		}
		if j <= 0 {
			mpd[i] = []string{strconv.Itoa(i + 1), parttenName, partten, "未找到匹配数据", "无"}
			i++
		}
		file.Close()
	}

	makeCsv(filename, mpd)
}

func makeCsv(fileName string, m map[int][]string) {
	// 不存在则创建;存在则清空;读写模式;
	file, err := os.Create(fileName)
	if err != nil {
		fmt.Println("open file is failed, err: ", err)
	}
	// 延迟关闭
	defer file.Close()

	// 写入UTF-8 BOM，防止中文乱码
	file.WriteString("\xEF\xBB\xBF")

	w := csv.NewWriter(file)

	// 写入数据
	w.Write([]string{"序号", "参数名称", "参数值", "原始数据", "时间"})
	w.Flush()

	// 按照key排序
	var keys []int
	for k := range m {
		keys = append(keys, k)
	}
	sort.Ints(keys)
	for _, key := range keys {
		w.Write(m[key])
		// 刷新缓冲
		w.Flush()
	}
}
func searchFile(partten, path, cmdparam string) (bb *bytes.Buffer, err error) {
	n := strings.Split(cmdparam, " ")
	psCmd := exec.Command(n[0], n[1], partten, path)
	grepStdout, psStderr := SetCommandStd(psCmd)
	err = psCmd.Run()
	if err != nil {
		err = errors.New(err.Error() + psStderr.String())
		return bb, err
	}
	return grepStdout, nil
}

//SetCommandStd sasasa
func SetCommandStd(cmd *exec.Cmd) (stdout, stderr *bytes.Buffer) {
	stdout = &bytes.Buffer{}
	stderr = &bytes.Buffer{}
	cmd.Stdout = stdout
	cmd.Stderr = stderr
	return stdout, stderr
}
