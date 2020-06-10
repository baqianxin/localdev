--shell
mkdir -p /data/nginx/logs/cr.mydomain.com/web
mkdir -p /data/nginx/logs/cr.mydomain.com/app
mkdir -p /home/q/system/cr.mydomain.com/logsCollect
mkdir -p /data/nginx/cache/cr.mydomain.com
mkdir -p /data/nginx/upload/cr.mydomain.com
mkdir -p /data/nginx/data/cr.mydomain.com

cp  -r *  /home/q/system/cr.mydomain.com/logsCollect
cp /usr/local/nginx/conf/include/cr.mydomain.com.conf.bak /usr/local/nginx/conf/include/cr.mydomain.com.conf
cp  ./webapp/conf/cr.jiagu.360.conf /usr/local/nginx/conf/include/cr.mydomain.com.conf
cp  ./webapp/conf/c.jiagu.360.conf /usr/local/nginx/conf/include/c.mydomain.com.conf



---pipeline


sh "mkdir -p /data/nginx/logs/cr.mydomain.com/web"
sh "mkdir -p /data/nginx/logs/cr.mydomain.com/app"
sh "mkdir -p /home/q/system/cr.mydomain.com/logsCollect"
sh "mkdir -p /data/nginx/cache/cr.mydomain.com"
sh "mkdir -p /data/nginx/upload/cr.mydomain.com"
sh "mkdir -p /data/nginx/data/cr.mydomain.com"

sh "mkdir -p /data/nginx/logs/c.mydomain.com/web"
sh "mkdir -p /data/nginx/logs/c.mydomain.com/app"
sh "mkdir -p /home/q/system/c.mydomain.com/logsCollect"
sh "mkdir -p /data/nginx/cache/c.mydomain.com"
sh "mkdir -p /data/nginx/upload/c.mydomain.com"
sh "mkdir -p /data/nginx/data/c.mydomain.com"

sh "cp  -r *  /home/q/system/cr.mydomain.com/logsCollect"
sh "cp  /home/q/system/cr.mydomain.com/logsCollect/webapp/conf/cr.jiagu.360.conf /usr/local/nginx/conf/include/cr.mydomain.com.conf"
sh "cp  /home/q/system/cr.mydomain.com/logsCollect/webapp/conf/c.jiagu.360.conf /usr/local/nginx/conf/include/c.mydomain.com.conf"


cr.mydomain.com.conf
sh "mv /usr/local/nginx/conf/include/cr.mydomain.com.conf.bak /usr/local/nginx/conf/include/cr.mydomain.com.conf"



echo "install..."
sh "cp  -r * /home/q/system/cr.mydomain.com/logsCollect"
sh "cp /usr/local/nginx/conf/include/cr.mydomain.com.conf.bak /usr/local/nginx/conf/include/cr.mydomain.com.conf"


fastcgi_param  WEB_LOG_DIR                     /data/nginx/logs/cr.mydomain.com/web/;
fastcgi_param  APP_LOG_DIR                     /data/nginx/logs/cr.mydomain.com/app/;
fastcgi_param  ACCESS_LOG_FILE                 /data/nginx/logs/cr.mydomain.com/web/cr.mydomain.com-access.log;
fastcgi_param  ERROR_LOG_FILE                  /data/nginx/logs/cr.mydomain.com/web/cr.mydomain.com-error.log;
fastcgi_param  DATA_DIR                        /data/nginx/data/cr.mydomain.com/;
fastcgi_param  CACHE_DIR                       /data/nginx/cache/cr.mydomain.com/;
fastcgi_param  UPLOAD_DIR                      /data/nginx/upload/cr.mydomain.com/;