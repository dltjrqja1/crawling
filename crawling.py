import requests
import re
import pandas as pd
from bs4 import BeautifulSoup

movie = pd.DataFrame({'title':[], 'age':[], 'Advance_rate':[], 'rating':[], 'genres':[]})
index = 0
print(movie)
def find_contents(dl,index):
    age = dl.find("span", {"class": age_re.search})
    title = dl.find("a", {"href": title_re.search})
    genres = dl.find_all("span", class_='link_txt')
    genre = str(genres[0].get_text())
    genre = genre.replace(',', "").replace("\t","").replace("\n","").replace("\r","")
    #genre_list = genre.split()
    num = dl.find_all("span", class_='num')
    grade = num[0]
    rating = ""
    if len(num) == 2:
        rate = num[1]
        rate = rate.get_text() if rate else "No Description"
        rating = rate
    tmp = dl.find_all("dd")
    run_time = ""
    for i in tmp:
        m = run_time_re.search(str(i))
        if m !=None:
            run_time = m[0]
            break
    age = age.get_text() if age else "No Description"
    title = title.get_text() if title else "No Description"
    grade = grade.get_text() if grade else "No Description"
    if rating !='':
        rating = float(rating)
    if grade !='':
        grade = float(grade)
    movie.loc[index] = {'title':title, 'age':age, 'Advance_rate':rating, 'rating':grade, 'genres':genre}
    index = index+1
    return index

requests = requests.get('https://movie.naver.com/movie/running/current.nhn')

soup = BeautifulSoup(requests.content, 'html.parser')

totals = soup.find_all('dl', class_='lst_dsc')


age_re = re.compile('ico_rating_*')
title_re = re.compile('/movie/bi/mi/basic.nhn*')
tag_del = re.compile('<+>')
run_time_re = re.compile('\d{2,3}분')
res = 0
for total in totals:
    index = find_contents(total,index)
    res = res+1
print(movie)
movie.to_csv('./movie_df.csv',encoding='utf-8-sig',sep=',')