## Docker-本地开发环境

```bahs
baqianxin@baqianxin-l3 MINGW64 /e/workspace
$ cd dev/ 

baqianxin@baqianxin-l3 MINGW64 /e/workspace/dev (dev)
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
```

### 基础服务
- nginx
- php
- go
- mysql
- redis
- elk


### 包含应用-扩展
  - filebeat : 日志文件收集工具，同步到ES，日志模板，kibana看板模板
  - mongo：存储PHP接口性能分析结果
  - xhgui：性能监控数据可视化
  - tideways：非侵入式监控服务PHP扩展
  - yaf：PHP扩展工作框架
  - beego:go语言Web服务框架，工作使用
  - phalcon：PHP扩展工作框架：以此为基础重构过web服务，二次框架设计
  - canal-go-client：canal日志消费者-go语言版本
  - tensorflow：深度学习框架
  - canal-server:msyql 二进制日志解析服务，可用于数据同步；查询以ES为主，MySQL数据变动同步到ES
  - tensorflow-server：模型部署服务
> nginx扩展有几个：headers-more-nginx-module....

### 服务编排

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
