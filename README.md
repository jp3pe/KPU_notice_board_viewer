# KPU_notice_board_viewer
## 한국산업기술대학교 교내 홈페이지의 학사공지 게시판을 DBMS에 파이썬으로 파싱해 C++로 열람하는 프로젝트
교내 **C++** 프로그래밍 프로젝트로 제작한 소스코드입니다.

**Docker** 컨테이너로 **DBMS(My SQL)** 을 구현했으며,
**Python(Beautiful Soup)** 로 웹 사이트 파싱을,
**C++** 로 DBMS Select 질의를 구현헀습니다.

**주석** 을 소스코드 내 삽입해 두었으니 혹시 궁금하신분은 직접 돌려보세요.

***

### 컴파일 및 실생 방법 안내
#### Docker
해당 설명은 Docker를 설치하고 로그인까지 완료해 dockerhub.comd에서 이미지 pull이 가능한 상태를 전제로 설명합니다.
##### Docker image 생성
	docker build -t kpu_bulletin_board_db .
##### Docker container 생성
	docker-compose up
	
	
#### Python
파이썬 명령어를 통해 가상환경을 생성하시는걸 추천드립니다.

**예시**

	python3 -m venv myvenv
	source (your_path_to_venv_derectory)/bin/activate
	pip install -r requirements.txt
	python paser.py
해당 명령어는 맥 이용자 기준입니다.


#### C++
C++을 컴파일하기 위해서 Clang++을 사용했으며 맥을 제외한 타 OS에서는 테스트를 해 보지 않았습니다.

해당 소스파일을 컴파일 하기 위해선 mysql-connector-c++ 라이브러리가 필요합니다.
전 brew 패키지 관리자를 이용해 설치했으며, 하단의 예시 명령어는 brew를 통해 설치된 라이브러리의 경로가 사용되었습니다.

**예시**

	clang++ --std=c++11 /usr/local/Cellar/mysql-connector-c++/8.0.18_1/lib/libmysqlcppconn8.dylib -g main.cpp -o main
