import requests
from bs4 import BeautifulSoup
import csv

# test GET page from url
page = requests.get('http://www.kpu.ac.kr/front/boardview.do?pkid=84137&currentPage=1&searchField=ALL&siteGubun=14&menuGubun=2&bbsConfigFK=1&searchLowItem=ALL&searchValue=')
# Test soupfy 
soup = BeautifulSoup(page.text, 'html.parser')
title = soup.find(class_='subject')

detail = soup.find(class_='article')
print(title.string)
print(detail.string)