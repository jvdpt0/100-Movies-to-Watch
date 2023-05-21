import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
movies_page = response.text
soup = BeautifulSoup(movies_page, 'html.parser')

movies = soup.find_all(name ='h3', class_='title')
movies_list = [movie.getText() for movie in reversed(movies)]

with open('movies_list.txt', 'w', encoding="utf-8") as f:
    for movie in movies_list:
        f.write(movie + "\n")