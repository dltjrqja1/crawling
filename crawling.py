import requests
import re
from bs4 import BeautifulSoup

requests = requests.get('https://movie.naver.com/movie/running/current.nhn?order=reserve')

soup = BeautifulSoup(requests.content, 'html.parser')

totals = soup.find_all('dl', class_='lst_dsc')


age_re = re.compile('ico_rating_*')
title_re = re.compile('/movie/bi/mi/basic.nhn*')
tag_del = re.compile('<+>')

def find_contents(dl):
    age = dl.find("span", {"class": age_re.search})
    title = dl.find("a", {"href": title_re.search})
    genres = dl.find_all("span", class_='link_txt')
    genre = str(genres[0].get_text())
    genre = genre.replace(',', "")
    genre_list = genre.split()
    print(age.get_text())
    print(title.get_text())
    print(genre_list)

for total in totals:
    find_contents(total)

#print(totals)