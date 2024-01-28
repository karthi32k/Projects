import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response_html = response.text
# print(response_text)

soup = BeautifulSoup(response_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
# print(all_movies)

movies_titles = [movie.getText() for movie in all_movies]
#print(movies_title)

movies_list = movies_titles[::-1]
#print(movies_list)

with open("MoviesList.txt", mode="w", encoding='utf-8') as file:
    for movie in movies_list:
        file.write(f"{movie}\n")
















# movies_titles = []

# for movie in soup.find_all(name="h3", class_="title"):
#     movies_titles.append(movie.getText())

# List comperhension
# all_movies = [movie.getText() for movie in movies_titles]

# Using for loop to get all movie
# for n in range(len(movies_titles)-1, -1, -1):
#     movie_list = movies_titles[n]
#     print(movie_list)

# # Using Slicing
# movies_list = all_movies[::-1]

# with open("MoviesList.txt", mode="w") as file:
#     for movie in movies_list:
#         file.write(f"{movie}\n")
