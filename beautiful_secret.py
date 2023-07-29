from urllib import request
from bs4 import BeautifulSoup
target=request.urlopen("https://www.weather.go.kr/w/index.do")
soup=BeautifulSoup(target, "html.parser")