FROM php:7.3-fpm
MAINTAINER oomcc <baqianxin@163.com>
ARG PHALCON_VERSION=3.4.2
ARG PHALCON_EXT_PATH=php7/64bits

RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
	&& echo "Asia/Shanghai" > /etc/timezone

RUN set -xe && \
        # Compile Phalcon
        curl -LO https://github.com/phalcon/cphalcon/archive/v${PHALCON_VERSION}.tar.gz && \
        tar xzf ${PWD}/v${PHALCON_VERSION}.tar.gz && \
        docker-php-ext-install -j $(getconf _NPROCESSORS_ONLN) ${PWD}/cphalcon-${PHALCON_VERSION}/build/${PHALCON_EXT_PATH} && \
        # Remove all temp files
        rm -r \
            ${PWD}/v${PHALCON_VERSION}.tar.gz \
            ${PWD}/cphalcon-${PHALCON_VERSION}


#ADD sources.list /etc/apt/sources.list
RUN apt-get update \
	# 相关依赖必须手动安装
	&& apt-get install -y \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
        supervisor \
        git \
    # 安装扩展
    && docker-php-ext-install -j$(nproc) iconv \
    # 如果安装的扩展需要自定义配置时
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd

RUN docker-php-ext-install pdo_mysql bcmath  \
    && docker-php-ext-enable pdo_mysql bcmath

RUN pecl install redis \
    && docker-php-ext-enable redis

COPY extension/docker-php-ext-tideways.ini /usr/local/etc/php/conf.d/docker-php-ext-tideways.ini
COPY extension/tideways_xhprof.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/tideways.so
COPY extension/docker-php-ext-mongodb.ini /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini
COPY extension/mongodb.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/mongodb.so

RUN apt-get clean \
    && apt-get autoremove

WORKDIR /opt

# Write Permission
RUN usermod -u 1000 www-data

EXPOSE 9000
VOLUME [ "/opt" ]
