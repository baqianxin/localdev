--shell
mkdir -p /data/nginx/logs/cr.jiagu.360.cn/web
mkdir -p /data/nginx/logs/cr.jiagu.360.cn/app
mkdir -p /home/q/system/cr.jiagu.360.cn/logsCollect
mkdir -p /data/nginx/cache/cr.jiagu.360.cn
mkdir -p /data/nginx/upload/cr.jiagu.360.cn
mkdir -p /data/nginx/data/cr.jiagu.360.cn

cp  -r *  /home/q/system/cr.jiagu.360.cn/logsCollect
cp /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf.bak /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf
cp  ./webapp/conf/cr.jiagu.360.conf /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf
cp  ./webapp/conf/c.jiagu.360.conf /usr/local/nginx/conf/include/c.jiagu.360.cn.conf



---pipeline


sh "mkdir -p /data/nginx/logs/cr.jiagu.360.cn/web"
sh "mkdir -p /data/nginx/logs/cr.jiagu.360.cn/app"
sh "mkdir -p /home/q/system/cr.jiagu.360.cn/logsCollect"
sh "mkdir -p /data/nginx/cache/cr.jiagu.360.cn"
sh "mkdir -p /data/nginx/upload/cr.jiagu.360.cn"
sh "mkdir -p /data/nginx/data/cr.jiagu.360.cn"

sh "mkdir -p /data/nginx/logs/c.jiagu.360.cn/web"
sh "mkdir -p /data/nginx/logs/c.jiagu.360.cn/app"
sh "mkdir -p /home/q/system/c.jiagu.360.cn/logsCollect"
sh "mkdir -p /data/nginx/cache/c.jiagu.360.cn"
sh "mkdir -p /data/nginx/upload/c.jiagu.360.cn"
sh "mkdir -p /data/nginx/data/c.jiagu.360.cn"

sh "cp  -r *  /home/q/system/cr.jiagu.360.cn/logsCollect"
sh "cp  /home/q/system/cr.jiagu.360.cn/logsCollect/webapp/conf/cr.jiagu.360.conf /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf"
sh "cp  /home/q/system/cr.jiagu.360.cn/logsCollect/webapp/conf/c.jiagu.360.conf /usr/local/nginx/conf/include/c.jiagu.360.cn.conf"


cr.jiagu.360.cn.conf
sh "mv /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf.bak /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf"



echo "install..."
sh "cp  -r * /home/q/system/cr.jiagu.360.cn/logsCollect"
sh "cp /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf.bak /usr/local/nginx/conf/include/cr.jiagu.360.cn.conf"


fastcgi_param  WEB_LOG_DIR                     /data/nginx/logs/cr.jiagu.360.cn/web/;
fastcgi_param  APP_LOG_DIR                     /data/nginx/logs/cr.jiagu.360.cn/app/;
fastcgi_param  ACCESS_LOG_FILE                 /data/nginx/logs/cr.jiagu.360.cn/web/cr.jiagu.360.cn-access.log;
fastcgi_param  ERROR_LOG_FILE                  /data/nginx/logs/cr.jiagu.360.cn/web/cr.jiagu.360.cn-error.log;
fastcgi_param  DATA_DIR                        /data/nginx/data/cr.jiagu.360.cn/;
fastcgi_param  CACHE_DIR                       /data/nginx/cache/cr.jiagu.360.cn/;
fastcgi_param  UPLOAD_DIR                      /data/nginx/upload/cr.jiagu.360.cn/;