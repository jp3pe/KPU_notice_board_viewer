# MySQL 최신 이미지를 기반으로 도커이미지를 생성한다.
FROM mysql:latest
# 크롤링 결과를 담기위한 테이블 생성문이 담긴 init.sql 파일을 도커 이미지에 복사
COPY MySQL/init.sql /docker-entrypoint-initdb.d/