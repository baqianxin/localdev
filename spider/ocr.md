# 基于开源模型的OCR中文提取

## 服务及模型地址

    git clone https://github.com/ouyanghuiyu/chineseocr_lite

## 服务环境    
    docker pull ufoym/deepo
    docker pull hub-mirror.c.163.com/ufoym/deepo
    docker run -it -p 6666:8080 -v data:/data --name ocr ufoym/deepo:latest 
    
    
    # docker-compose
    version: "3.1"
    services:
        ocr:
            image: ufoym/deepo:latest
            container_name: ocr
            ports:
            - "8080:8080"
            volumes:
            - ./data:/data
## 运行
    cd /data/chineseocr_lite
    pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requiremen
    app.py 8080

## 示例
 ![demo](https://note.youdao.com/yws/api/personal/file/9F930009C2F74EC8AD6C898C3BFF6DAF?method=download&shareKey=7be2dd8f1f2e38a268610419291a3707)

## 接口分析

## 模型训练

