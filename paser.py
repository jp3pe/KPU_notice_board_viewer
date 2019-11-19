import requests
from bs4 import BeautifulSoup
import csv

# URL로 get요청을 한다.
page = requests.get('http://www.kpu.ac.kr/front/boardview.do?pkid=84137&currentPage=1&searchField=ALL&siteGubun=14&menuGubun=2&bbsConfigFK=1&searchLowItem=ALL&searchValue=')
# get 요청으로 들어온 텍스트를 beautifulsoup의 트리 구조로 변경한다.
soup = BeautifulSoup(page.text, 'html.parser')
# 트리 구조중 제목(class가 subject)을 추출한다.
title = soup.find(class_='subject')
print(title.string)

# 본문을 찾아 저장한다.
details = soup.find(class_='article')
for detail in details.stripped_strings:
    print(detail)