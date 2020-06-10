## Docker-本地开发环境

```bash

oom@oom-l3 MINGW64 /e/workspace/dev (dev)
$ docker-compose start
Starting go       ... done
Starting mysql    ... done
Starting redis    ... done
Starting mongodb  ... done
Starting php      ... done
Starting nginx    ... done
Starting elk      ... done
Starting filebeat ... done
Starting canal    ... done
Starting airflow    ... done
Starting flink    ... done
```

### 基础服务
- nginx
- php
- go
- mysql
- redis
- elk


### 我的应用-扩展
  - Hadoop : 暂未集成（用于打点日志的存储，统计）
  - Kafka ：消息队列，存储打点日志信息
  - Lua : (OpenResty) 提供打点接口，逻辑简单，调用频繁，日志数据落地到文件-Kafka
  - Spark : MapReduce封装，用于日志数据的清洗
  - flink : 实时流计算服务（用于日志打点收集，统计PV/UV数据）
  - airflow : 分布式任务（DAG有向无环图）调度服务（批量大数据处理任务调度 收集->清洗->拆分->过滤->统计->其他业务操作...） 
  - filebeat : 日志文件收集工具，同步到 ES，日志模板，kibana看板模板
  - mongo：存储 PHP 接口性能分析结果
  - xhgui：性能监控数据可视化
  - tideways：非侵入式监控服务 PHP 扩展
  - yaf：PHP 扩展工作框架
  - beego: go 语言 Web 服务框架，工作使用
  - phalcon：PHP 扩展工作框架：以此为基础重构过 web 服务，二次框架设计
  - tensorflow：深度学习框架
  - canal-server: msyql 二进制日志解析服务，可用于数据同步；（eg.部分业务查询以ES为主，MySQL数据变动同步到ES)（canal-go-client：canal 日志消费者-go版本）
  - tensorflow-server：模型部署服务
  - manim: LaTex -> Animation Video 数学老师[ Grant ](https://www.3blue1brown.com)的视频制作工具
  - - LaTeX:文档编排
  - - ImageMagic : [图片处理](https://imagemagick.org/script/download.php)
  - - FFmpeg : [视频处理](http://www.ffmpeg.org/download.html)
> nginx 扩展：headers-more-nginx-module....

```
LaTeX:
    Lambda

视频文件转换为 gif 图片 ffmpeg
ffmpeg -i output/OpeningManimExample.mp4   -r 15 -vf fps=15,scale=700:-1   output/OpeningManimExample.gif 

压缩 gif 图片 ImageMagic
convert -fuzz 15% OpeningManimExample.gif -layers Optimize op_ome.gif
```

### 基础服务编排

```yml
version: "3.1"
services:
  nginx:
    build: ./server/nginx
    container_name: nginx
    ports:
      - "80:80"
    links:
      - "php"
      - "mongodb"
    volumes:
      - ./logs:/opt/logs
      - ./www:/opt/htdocs
      - ./config/nginx/conf.d:/etc/nginx/conf.d:rw
      - ./config/nginx/nginx.conf:/etc/nginx/nginx.conf

  php:
    build: ./server/php
    container_name: php7
    ports:
      - "9000:9000"
    links:
      - "mysql"
      - "redis"
      - "mongodb"
    volumes:
      - ./www/quclient:/home/q/php/quclient
      - ./config/php/php.ini:/usr/local/etc/php/php.ini
      - ./config/php/php-fpm/www.conf:/usr/local/etc/php-fpm.d/www.conf
      - ./www:/opt/htdocs
      - ./logs:/opt/logs
  go:
    build: ./server/go
    ports:
      - 88:88
    volumes:
      - ./www/goproject:/go/src/project
  mysql:
    build: ./server/mysql
    container_name: mysql5.7
    ports:
      - "3306:3306"
    volumes:
      - ./config/mysql/mysqld.conf:/etc/mysql/mysql.conf.d
      - ./data/mysql:/var/lib/mysql
      - ./logs:/opt/logs
    environment:
      MYSQL_ROOT_PASSWORD: 123456
    restart:
      always

  redis:
    build: ./server/redis
    ports:
      - "6379:6379"

  mongodb:
    image: mongo
    ports:
      - "27017:27017"
    volumes:
      - /mongodata:/data/db

  elk:
    image: sebp/elk
    volumes:
      - ./logs/elasticsearch:/opt/elasticsearch/logs
      - ./config/elk/kibana.yml:/opt/kibana/config/kibana.yml
    ports:
      - "5601:5601"
      - "9200:9200"
      - "5044:5044"

  filebeat:
    image: docker.elastic.co/beats/filebeat:7.3.1
    volumes:
      - ./logs:/opt/logs
      - ./config/filebeat/filebeat.yml:/usr/share/filebeat/filebeat.yml
      - ./config/filebeat/modules.d:/usr/share/filebeat/modules.d
    links:
      - elk
    environment:
      KIBANA_HOST: 'elk:5601'
      ELASTICSEARCH_HOSTS: 'elk:9200'
      ELASTICSEARCH_USERNAME: ''
      ELASTICSEARCH_PASSWORD: ''

  canal:
    image: canal/canal-server
    ports:
      - 2222:2222
      - 8000:8000
      - 11111:11111
      - 11112:11112
    links:
      - mysql
    environment:
      canal.destinations: 'test'
      canal.instance.master.address: 'mysql:3306'
      canal.instance.dbUsername: 'canal'
      canal.instance.dbPassword: 'canal'
      canal.instance.connectionCharset: 'UTF-8'
      canal.instance.tsdb.enable: 'true'
      canal.instance.gtidon: 'false'

```
