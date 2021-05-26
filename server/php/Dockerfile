FROM php:7.3-fpm
MAINTAINER oomcc <baqianxin@163.com>
ARG PHALCON_VERSION=3.4.2
ARG PHALCON_EXT_PATH=php7/64bits
ADD sources.list /etc/apt/sources.list
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

RUN apt-get update \
	# 相关依赖必须手动安装
	&& apt-get install -y --allow-downgrades \
        libzip-dev zlib1g-dev zlib1g=1:1.2.8.dfsg-2+b1 \
        libfreetype6-dev \
        libjpeg62-turbo-dev \
        libmcrypt-dev \
        libpng-dev \
    # 安装扩展
    && docker-php-ext-install -j$(nproc) iconv opcache \
    # 如果安装的扩展需要自定义配置时
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/ \
    && docker-php-ext-install -j$(nproc) gd




RUN apt-get update && apt-get install -y

RUN docker-php-ext-install pdo_mysql \
    && docker-php-ext-enable pdo_mysql

RUN pecl install redis yaf zip \
    && docker-php-ext-enable redis yaf zip

COPY extension/docker-php-ext-tideways.ini /usr/local/etc/php/conf.d/docker-php-ext-tideways.ini
COPY extension/tideways_xhprof.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/tideways.so
COPY extension/docker-php-ext-mongodb.ini /usr/local/etc/php/conf.d/docker-php-ext-mongodb.ini
COPY extension/mongodb.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/mongodb.so
COPY extension/docker-php-ext-yaf.ini /usr/local/etc/php/conf.d/docker-php-ext-yaf.ini
COPY extension/mysqli.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/mysqli.so
COPY extension/pcntl.so /usr/local/lib/php/extensions/no-debug-non-zts-20180731/pcntl.so

ENV LIBRDKAFKA_VERSION v0.9.5
ENV BUILD_DEPS \
        build-essential \
        libssl-dev \
        python-minimal \
        zlib1g-dev wget unzip
RUN apt-get update \
    && apt-get install -y --no-install-recommends ${BUILD_DEPS} \
    && cd /tmp \
    && wget https://codeload.github.com/edenhill/librdkafka/zip/master \
    && unzip master && cd librdkafka-master \
    # && git clone \
    #     --branch ${LIBRDKAFKA_VERSION} \
    #     --depth 1 \
    #     https://github.com/edenhill/librdkafka.git \
    # && cd librdkafka \
    && ./configure \
    && make \
    && make install \
    && pecl install rdkafka \
    && docker-php-ext-enable rdkafka \
    && rm -rf /tmp/librdkafka \
    && apt-get purge \
        -y --auto-remove \
        -o APT::AutoRemove::RecommendsImportant=false \
        ${BUILD_DEPS}

RUN apt-get clean \
    && apt-get autoremove

WORKDIR /opt

# Write Permission
RUN usermod -u 1000 www-data

EXPOSE 9000
VOLUME [ "/opt" ]
