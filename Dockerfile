FROM mysql:latest
COPY MySQL/init.sql /docker-entrypoint-initdb.d/