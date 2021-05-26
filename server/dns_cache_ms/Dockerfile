FROM r.addops.soft.360.cn/library/nginx-19-el6:latest
RUN uname -a 
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo '$TZ' > /etc/timezone

RUN yum install epel-release yum-utils supervisor \
    lua-devel readline-devel pcre-devel openssl-devel libxml2-dev \
    libxslt-devel  gd-devel  GeoIP GeoIP-devel GeoIP-data -y

RUN cd /opt/ && curl -L -O http://nginx.org/download/nginx-1.18.0.tar.gz && tar zxvf nginx-1.18.0.tar.gz > /dev/null \
    && mkdir -p /opt/nginx-1.18.0/modules && cd /opt/nginx-1.18.0/modules  \
    && wget https://github.com/simplresty/ngx_devel_kit/archive/v0.3.0.tar.gz && tar zxvf v0.3.0.tar.gz > /dev/null \
    && wget https://github.com/openresty/lua-nginx-module/archive/v0.10.13.tar.gz && tar zxvf v0.10.13.tar.gz > /dev/null \
    && wget https://github.com/openresty/srcache-nginx-module/archive/v0.28.tar.gz && tar zxvf v0.28.tar.gz > /dev/null \
    &&  wget https://github.com/openresty/echo-nginx-module/archive/v0.62.tar.gz && tar zxvf v0.62.tar.gz > /dev/null \
    && wget https://github.com/FRiCKLE/ngx_cache_purge/archive/2.3.tar.gz && tar zxvf 2.3.tar.gz > /dev/null \
    && wget https://github.com/fdintino/nginx-upload-module/archive/2.3.0.tar.gz  && tar zxvf 2.3.0.tar.gz > /dev/null \
    && wget https://github.com/masterzen/nginx-upload-progress-module/archive/v0.9.2.tar.gz && tar zxvf v0.9.2.tar.gz > /dev/null \
    &&  wget https://github.com/openresty/headers-more-nginx-module/archive/v0.33.tar.gz && tar zxvf v0.33.tar.gz > /dev/null \
    && wget https://github.com/openresty/memc-nginx-module/archive/v0.19.tar.gz && tar zxvf v0.19.tar.gz > /dev/null \ 
    && wget http://luajit.org/download/LuaJIT-2.0.5.tar.gz && tar -zxvf  LuaJIT-2.0.5.tar.gz > /dev/null \
    && cd LuaJIT-2.0.5 \
    && make install PREFIX=/usr/local/LuaJIT \
    && echo 'export LUAJIT_LIB=/usr/local/LuaJIT/lib' >> /etc/profile \
    && echo 'export LUAJIT_INC=/usr/local/LuaJIT/include/luajit-2.0' >> /etc/profile && source /etc/profile
    
RUN ls -al /opt/nginx-1.18.0/modules

COPY ngx_http_full_log_module/* /opt/nginx-1.18.0/modules/ngx_http_full_log_module/

WORKDIR /opt/nginx-1.18.0

RUN wget https://www.openssl.org/source/openssl-1.0.1u.tar.gz && tar zxvf openssl-1.0.1u.tar.gz > /dev/null 

RUN cd /opt/nginx-1.18.0 && ./configure  \
    --prefix=/usr/local/nginx \
    --error-log-path=/data/nginx/logs/error.log \
    --pid-path=/var/run/nginx.pid \
    --lock-path=/var/lock/nginx.lock \
    --http-log-path=/data/nginx/logs/access.log \
    --http-client-body-temp-path=/data/nginx/client_body_temp \
    --http-proxy-temp-path=/data/nginx/proxy_temp \
    --http-fastcgi-temp-path=/data/nginx/fastcgi_temp \
    --http-uwsgi-temp-path=/data/nginx/uwsgi_temp \
    --http-scgi-temp-path=/data/nginx/scgi_temp \
    --with-http_ssl_module \
    --with-http_v2_module \
    --with-http_realip_module \
    --with-http_addition_module \
    --with-http_xslt_module \
    --with-http_image_filter_module \
    --with-http_geoip_module\
    --with-http_sub_module \
    --with-http_dav_module \
    --with-http_flv_module \
    --with-http_mp4_module \
    --with-http_gunzip_module \
    --with-http_gzip_static_module \
    --with-http_auth_request_module \
    --with-http_random_index_module \
    --with-http_secure_link_module \
    --with-http_degradation_module \
    --with-http_slice_module \
    --with-http_stub_status_module \
    --with-stream \
    --with-stream_ssl_module \
    --with-google_perftools_module \
    --with-openssl=openssl-1.0.1u \
    --with-debug \
    --with-pcre \
    --with-pcre-jit \
    --add-module=modules/nginx-upload-module-2.3.0 \
    --add-module=modules/nginx-upload-progress-module-0.9.2 \
    --add-module=modules/lua-nginx-module-0.10.13 \
    --add-module=modules/ngx_devel_kit-0.3.0 \
    --add-module=modules/srcache-nginx-module-0.28 \
    --add-module=modules/echo-nginx-module-0.62 \
    --add-module=modules/ngx_cache_purge-2.3 \
    --add-module=modules/headers-more-nginx-module-0.33 \
    --add-module=modules/ngx_http_full_log_module \
    --add-module=modules/memc-nginx-module-0.19 > /dev/null
# --add-module=modules/passenger-5.0.27/src/nginx_module 

RUN make >/dev/null && make install 

RUN rpm --rebuilddb && yum install http://rpms.remirepo.net/enterprise/remi-release-6.rpm -y
RUN rpm --rebuilddb && yum install -y  php73-php-devel php73-php-pear php73-php-fpm php73-php-cli php73-php-bcmath php73-php-gd \
    php73-php-json php73-php-mbstring php73-php-mcrypt php73-php-mysqlnd php73-php-opcache \
    php73-php-pdo php73-php-pecl-crypto php73-php-pecl-mcrypt php73-php-pecl-geoip php73-php-rdkafka \
    php73-php-pecl-swoole php73-php-recode php73-php-snmp php73-php-soap php73-php-xmll php73-php-pecl-mongodb -y
RUN find /etc/opt/remi/php73 -name php.ini && ln -s /opt/remi/php73/root/usr/bin/php /usr/bin/php \
    && ln -s /opt/remi/php73/root/usr/bin/pecl /usr/bin/pecl \
    && ln -s /opt/remi/php73/root/usr/bin/php-config /usr/bin/php-config \
    && ln -s /opt/remi/php73/root/usr/bin/phpize /usr/bin/phpize \
    && sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/' /etc/opt/remi/php73/php.ini \
    && sed -i 's/;memory_limit = 128M/memory_limit = 512M/' /etc/opt/remi/php73/php.ini \
    && sed -i 's/;memory_limit = 128M/memory_limit = 512M/' /etc/opt/remi/php73/php.ini \
    && sed -i 's/user = apache/user = root/' /etc/opt/remi/php73/php-fpm.d/www.conf  \
    && sed -i 's/group = apache/group = root/' /etc/opt/remi/php73/php-fpm.d/www.conf \
    && sed -i 's/;clear_env = no/clear_env = no/' /etc/opt/remi/php73/php-fpm.d/www.conf

RUN rpm -e --nodeps autoconf-2.63 \
    && curl -L -O http://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz \
    && tar zxf autoconf-2.69.tar.gz \
    && cd autoconf-2.69 && ./configure --prefix=/usr/ && make && make install

RUN wget https://github.com/tideways/php-xhprof-extension/archive/v5.0.2.tar.gz && tar zxvf v5.0.2.tar.gz > /dev/null \
    && cd php-xhprof-extension-5.0.2 && phpize && ./configure > /dev/null && make && make install \
    && echo 'extension=tideways_xhprof.so' >> /etc/opt/remi/php73/php.d/tideways_xhprof.ini \
    && echo 'tideways.auto_prepend_library=0'>> /etc/opt/remi/php73/php.d/tideways_xhprof.ini \
    && wget https://github.com/baqianxin/xhgui-branch/archive/v1.0.6.tar.gz > /dev/null \
    && tar zxvf v1.0.6.tar.gz > /dev/null && cp -r xhgui-branch-1.0.6 /home/q/system/xhgui \
    && cd /home/q/system/xhgui && php install.php > /dev/null

WORKDIR /home/q/system   
RUN yum clean all && rm -rf /opt/nginx-1.18.0 && rm -f /opt/nginx-1.18.0.tar.gz
COPY nginx.conf /usr/local/nginx/conf/nginx.conf

COPY autoup /bin/autoup

ENTRYPOINT "/bin/autoup"