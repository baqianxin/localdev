FROM gitlab/gitlab-runner:latest

LABEL MAINTAINER=baqianxin@360.cn

RUN export LANG=en_US.UTF-8  && export LANGUAGE=en_US

RUN apt-get update && \
    apt-get  install -y  nodejs vim unzip 
RUN cd /opt && wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.0.0.1744-linux.zip && \
    unzip sonar-scanner-cli-4.0.0.1744-linux.zip && mv sonar-scanner-4.0.0.1744-linux sonar-scanner

RUN  ln -s /opt/sonar-scanner/bin/sonar-scanner /usr/bin/sonar-scanner && sonar-scanner -v
