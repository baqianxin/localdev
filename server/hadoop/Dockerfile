FROM ubuntu:14.04

MAINTAINER oomcc <baqianxin@163.com>
RUN mkdir -p /opt
WORKDIR /opt

ADD sources.list /etc/apt/sources.list
ADD etc/sshd_config /opt/sshd_config
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && echo "Asia/Shanghai" > /etc/timezone

RUN sudo apt-get install -f apt && sudo apt-get update -y
RUN sudo apt-get install -y wget ssh

RUN mkdir -p /opt/hadoop/ && cd /opt/hadoop
RUN wget http://mirrors.sonic.net/apache/hadoop/common/hadoop-2.6.5/hadoop-2.6.5.tar.gz 
RUN tar -xvzf Hadoop-2.6.5.tar.gz
RUN  echo 'export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64' >>  ~/.bashrc \
    && echo 'export HADOOP_HOME=/root/soft/apache/hadoop/hadoop-2.6.5' >>  ~/.bashrc \
    && echo 'export HADOOP_CONFIG_HOME=$HADOOP_HOME/etc/hadoop ' >>  ~/.bashrc \
    && echo 'export PATH=$PATH:$HADOOP_HOME/bin ' >>  ~/.bashrc \
    && echo 'export PATH=$PATH:$HADOOP_HOME/sbin' >>  ~/.bashrc \
    && echo '/usr/sbin/sshd' >> ~/.bashrc
RUN source ~/.bashrc
RUN mkdir -p ~/var/run/sshd && cd ~/ \
    && ssh-keygen -t rsa -P '' -f ~/.ssh/id_dsa \
    && cd .ssh && cat id_dsa.pub >> authorized_keys

RUN mv /opt/sshd_config /etc/ssh/sshd_config


