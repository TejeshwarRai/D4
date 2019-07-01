# import requests as rq
# from bs4 import BeautifulSoup

# url = "https://twitter.com/dna"
# response = rq.get(url)
# # print(response.text)
#
# soup = BeautifulSoup(response.text, "html.parser")
# print(type(soup))
# # print(soup)
# # print(soup.prettify())
#
# print(soup.title.text)
# print()

import requests as rq
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://www.imdb.com/india/top-rated-indian-movies/"
response = rq.get(url)

soup = BeautifulSoup(response.text, "html.parser")

tags = soup.find_all("span", class_="secondaryInfo")

movies = []

for tag in tags:
    data = tag.text
    movies.append(data.strip())


for movie in movies:
    print(movie)
    print("*******")



tagse = soup.find_all("td", class_="ratingColumn imdbRating")
moviese = []

for tage in tagse:
    datae = tage.text
    moviese.append(datae.strip())


for moviee in moviese:
    print(moviee)
    print("*******")

plt.bar(movies,moviese)
plt.show()