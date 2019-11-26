from bs4 import BeautifulSoup
import requests


# 공지사항 URL을 저장하기 위한 변수 선언
university_bulletin_board_url1 = 'http://www.kpu.ac.kr/front/boardlist.do?currentPage='
page_num = 1
university_bulletin_board_url2 = '&menuGubun=1&siteGubun=14&bbsConfigFK=1&searchField=ALL&searchValue=&searchLowItem=ALL'
page = requests.get(university_bulletin_board_url1 + str(page_num) + university_bulletin_board_url2)
# 페이지 URL이 정상적으로 만들어 졌는지 확인하는 코드
# print(university_bulletin_board_url1 + str(page_num) + university_bulletin_board_url2)
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

# a 태그 중 href 속성이 값을 가진 경우
for a in soup.find_all('a', href=True):
    # 첨부파일 링크인 경우
    if '/Download' in a['href']:
        pass
    else:
        # 의미없는 href속성의 경로를 제거한다.
        url = str(a['href']).replace("/viewcount.do?rtnUrl=", "")
        # 원래 URL형식으로 특수문자를 변환한다.
        url = url.replace("^","&")
        urls.append(url)
        
# 제목을 추출하는 코드
# 제목을 저장하는 span의 class가 text인 경우
for s in soup.find_all('span', {'class' : 'text'}):
    sp = str(s)
    # 의미없는 특수 문자들을 제거한다.
    sp = sp.replace("\r", "")
    sp = sp.replace("\n", "")
    sp = sp.replace("\t", "")
    # 제목 앞 부분까지를 제거한다.
    sp = sp.replace("<span class=\"text\">", "")
    # 제목 뒷 부분을 제거한다.
    sp = sp.replace("</span>", "")
    titles.append(sp)

# 해당 페이지의 파싱한 결과물들을 출력
for i in range(len(titles)):
    print(f"{titles[i]} : ", end="\n")
    print("http://www.kpu.ac.kr"+urls[i], end="\n\n")

### 게시판 내 게시글을 긁어오는 소스 예제 ###
# # URL로 get요청을 한다.
# page = requests.get('http://www.kpu.ac.kr/front/boardview.do?pkid=84137&currentPage=1&searchField=ALL&siteGubun=14&menuGubun=2&bbsConfigFK=1&searchLowItem=ALL&searchValue=')
# # get 요청으로 들어온 텍스트를 beautifulsoup의 트리 구조로 변경한다.
# soup = BeautifulSoup(page.text, 'html.parser')
# # 트리 구조중 제목(class가 subject)을 추출한다.
# title = soup.find(class_='subject')
# print(title.string)

# # 본문을 찾아 저장한다.
# details = soup.find(class_='article')
# for detail in details.stripped_strings:
#     print(detail)
### 게시판 내 게시글을 긁어오는 소스 예제 ###
