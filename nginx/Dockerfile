FROM centos:centos7
MAINTAINER oom <baqianxin@163.com>

ENV TZ "Asia/Shanghai"

#Yum
RUN yum -y update && \
    yum install -y gcc automake autoconf libtool make gcc-c++ vixie-cron  wget zlib  file openssl-devel sharutils zip  bash vim cyrus-sasl-devel libmemcached libmemcached-devel libyaml libyaml-devel unzip libvpx-devel openssl-devel ImageMagick-devel  autoconf  tar gcc libxml2-devel gd-devel libmcrypt-devel libmcrypt mcrypt mhash libmcrypt libmcrypt-devel libxml2 libxml2-devel bzip2 bzip2-devel curl curl-devel libjpeg libjpeg-devel libpng libpng-devel freetype-devel bison libtool-ltdl-devel net-tools && \
    yum clean all

RUN mkdir -p /var/log/nginx && \
    mkdir -p /var/cache/nginx && \
    mkdir -p /var/run && \
    useradd -s /sbin/nologin -M nginx

COPY resources/headers-more-nginx-module-0.33.tar.gz /tmp/htdocs/headers-more-nginx-module-0.33.tar.gz
COPY resources/nginx-1.15.12.tar.gz /tmp/htdocs/nginx-1.15.12.tar.gz

RUN mkdir -p /tmp/htdocs/headers-more-nginx-module \
        && tar -xf /tmp/htdocs/headers-more-nginx-module-0.33.tar.gz -C /tmp/htdocs/headers-more-nginx-module --strip-components=1 \
        && rm /tmp/htdocs/headers-more-nginx-module-0.33.tar.gz

RUN mkdir -p /tmp/htdocs/nginx-1.15.12 \
        && tar -xf /tmp/htdocs/nginx-1.15.12.tar.gz -C /tmp/htdocs/nginx-1.15.12 --strip-components=1 \
        && rm /tmp/htdocs/nginx-1.15.12.tar.gz

#Nginx
RUN cd /tmp/htdocs/nginx-1.15.12 && \
    ./configure \
     --prefix=/etc/nginx \
     --sbin-path=/usr/sbin/nginx \
     --modules-path=/usr/lib/nginx/modules \
     --conf-path=/etc/nginx/nginx.conf \
     --error-log-path=/var/log/nginx/error.log \
     --http-log-path=/var/log/nginx/access.log \
     --pid-path=/var/run/nginx.pid \
     --lock-path=/var/run/nginx.lock \
     --http-client-body-temp-path=/var/cache/nginx/client_temp \
     --http-proxy-temp-path=/var/cache/nginx/proxy_temp \
     --http-fastcgi-temp-path=/var/cache/nginx/fastcgi_temp \
     --http-uwsgi-temp-path=/var/cache/nginx/uwsgi_temp \
     --http-scgi-temp-path=/var/cache/nginx/scgi_temp \
     --user=nginx \
     --group=nginx \
     --with-compat \
     --with-file-aio \
     --with-threads \
     --with-http_addition_module \
     --with-http_auth_request_module \
     --with-http_dav_module \
     --with-http_flv_module \
     --with-http_gunzip_module \
     --with-http_gzip_static_module \
     --with-http_mp4_module \
     --with-http_random_index_module \
     --with-http_realip_module \
     --with-http_secure_link_module \
     --with-http_slice_module \
     --with-http_ssl_module \
     --with-http_stub_status_module \
     --with-http_sub_module \
     --with-http_v2_module \
     --with-mail \
     --with-mail_ssl_module \
     --with-stream \
     --with-stream_realip_module \
     --with-stream_ssl_module \
     --with-stream_ssl_preread_module \
     --add-module=/tmp/htdocs/headers-more-nginx-module && \
     make && \
     make install

COPY resources/etc/nginx/nginx.conf /etc/nginx/nginx.conf
COPY resources/etc/nginx/fastcgi_params /etc/nginx/fastcgi_params

EXPOSE 80 443
#启动nginx
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]
