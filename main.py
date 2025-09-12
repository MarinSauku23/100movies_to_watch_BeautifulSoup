import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url=URL)
response.encoding = "utf-8"
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movies_list = []

for num in range(len(all_movies)):
    movies_list.append(all_movies[num].getText())
movies_list.reverse()


for movie in movies_list:
    with open("movies.txt", "a", encoding="utf-8") as file:
        file.write(f"{movie}\n")






