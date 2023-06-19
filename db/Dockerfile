FROM mysql/mysql-server:latest
COPY ./init.sql /docker-entrypoint-initdb.d
RUN chmod -R 777 /var/lib/mysql/