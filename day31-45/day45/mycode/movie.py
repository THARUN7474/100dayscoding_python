import  requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

resp = requests.get(URL)
website_html = resp.text
website_soup = BeautifulSoup(website_html,"html.parser")
# print(website_soup("title"))
# print(website_soup.find_all("a"))
all_names = website_soup.find_all(name="h3", class_="title")
movie_list = []
for name in all_names:
    print(name.getText())
    movie_list.append(name.getText())
    with open("movies.txt", "a",errors= "ignore") as file:
        file.write(f"{name.getText()} \n")
print(movie_list[::-1])