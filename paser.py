from bs4 import BeautifulSoup
import requests
import mysql.connector

kpu = mysql.connector.connect(
    host="localhost",
    port="53306",
    user="root",
    passwd="qwer1234",
    database = "kpu"
)

mycursor = kpu.cursor()

sql = "Insert Into bulletin_board(title, content) Values(%s, %s)"

# 공지사항 URL을 저장하기 위한 변수 선언
university_bulletin_board_url1 = 'http://www.kpu.ac.kr/front/boardlist.do?currentPage='
page_num = 1
university_bulletin_board_url2 = '&menuGubun=1&siteGubun=14&bbsConfigFK=1&searchField=ALL&searchValue=&searchLowItem=ALL'

# 반복문을 통해서 페이지 접근
for page_num in range(1, 6):
    page = requests.get(university_bulletin_board_url1 +
                        str(page_num) + university_bulletin_board_url2)
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.table

    table = str(table)
    # table 변수 내 특수기호 제거
    table = table.replace("\n", "")
    table = table.replace("\t", "")
    table = table.replace("\r", "")

    html = table
    soup = BeautifulSoup(html, 'html.parser')
    urls = []
    titles = []
    details = []

    # a 태그 중 href 속성이 값을 가진 경우
    for a in soup.find_all('a', href=True):
        # 첨부파일 링크인 경우
        if '/Download' in a['href']:
            pass
        else:
            # 의미없는 href속성의 경로를 제거한다.
            url = str(a['href']).replace("/viewcount.do?rtnUrl=", "")
            # 원래 URL형식으로 특수문자를 변환한다.
            url = url.replace("^", "&")
            if url in urls:
                continue
            else:
                urls.append(url)

    for i in range(len(urls)):
        page = requests.get("http://www.kpu.ac.kr" + str(urls[i]))
        soup = BeautifulSoup(page.text, 'html.parser')
        # 제목을 리스트에 저장
        title = soup.find(class_='subject')
        titles.append(title.string)
        # 본문을 리스트에 저장
        article = soup.find(class_='article')
        details.append(article.text)

        # SQL 구문을 통한 DBMS 접근
        val = (titles[i], details[i])
        mycursor.execute(sql, val)
        kpu.commit()
