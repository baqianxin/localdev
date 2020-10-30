FROM r.addops.soft.360.cn/library/nginx-19-el6:latest
RUN  uname -a 
RUN yum install epel-release yum-utils -y
RUN yum install http://rpms.remirepo.net/enterprise/remi-release-6.rpm -y
RUN yum install -y php73-php-fpm php73-php-cli php73-php-bcmath php73-php-gd php73-php-json php73-php-mbstring php73-php-mcrypt php73-php-mysqlnd php73-php-opcache php73-php-pdo php73-php-pecl-crypto php73-php-pecl-mcrypt php73-php-pecl-geoip php73-php-pecl-swoole php73-php-recode php73-php-snmp php73-php-soap php73-php-xmll -y
RUN find /etc/opt/remi/php73 -name php.ini && ln -s /opt/remi/php73/root/usr/bin/php /usr/bin/php
RUN sed -i 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/' /etc/opt/remi/php73/php.ini
RUN sed -i 's/;memory_limit = 128M/memory_limit = 512M/' /etc/opt/remi/php73/php.ini
RUN sed -i 's/;memory_limit = 128M/memory_limit = 512M/' /etc/opt/remi/php73/php.ini
RUN sed -i 's/;user = apache/user = nobody/' /etc/opt/remi/php73/php-fpm.d/www.conf
RUN sed -i 's/;group = apache/group = nobody/' /etc/opt/remi/php73/php-fpm.d/www.conf
COPY nginx.conf /usr/local/nginx/conf/nginx.conf
COPY autoup /bin/autoup

RUN chkconfig --add php73-php-fpm && chkconfig php73-php-fpm on

ENTRYPOINT "/bin/autoup"