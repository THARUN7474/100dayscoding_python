from bs4 import BeautifulSoup

# import lxml

with open("website.html", errors='ignore') as file:
    content = file.read()

soup = BeautifulSoup(content,"html.parser")
#
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.p)
# print(soup.a)
# print(soup)
# print(soup)
# print(soup.prettify())


all_achor_tags = soup.find_all("a")
print(all_achor_tags)
for tag in all_achor_tags:
    # print(tag.getText)
    print(tag.get("href"))
    # print(tag.string)

section_heading = soup.find(name="h3",class_="heading")
print(section_heading)
print(section_heading.name)
print(section_heading.string)


# to narrowdown search we cacn use css selectors


selecting_a = soup.select_one(selector="p a")
selecting_b = soup.select_one(selector="#name")
selecting_c = soup.select_one(selector=".heading")
print(f"{selecting_a}\n {selecting_b}\n{selecting_c}")