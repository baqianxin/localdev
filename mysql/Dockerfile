FROM hub.c.163.com/library/mysql:latest

# Write Permission
RUN usermod -u 1000 mysql && chown mysql.mysql /var/run/mysqld/

EXPOSE 3306
VOLUME [ "/opt" ]