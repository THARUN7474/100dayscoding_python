import requests
from bs4 import BeautifulSoup

resp = requests.get("https://news.ycombinator.com/")
# print(resp.text)
webpage_content = resp.text

Webpage_soupcontent = BeautifulSoup(webpage_content,"html.parser")

# print(Webpage_soupcontent("title"))

article_titles = []
article_links = []
for article_tag in Webpage_soupcontent.find_all(name="span", class_="titleline"):
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.find("a")["href"])


article_upvotes = []
for article in Webpage_soupcontent.find_all(name="td", class_="subtext"):
    if article.span.find(class_="score") is None:
        article_upvotes.append(0)
    else:
        article_upvotes.append(int(article.span.find(class_="score").contents[0].split()[0]))

# print(article_upvotes)
# print(article_links)
# print(article_titles)
max_points_index = article_upvotes.index(max(article_upvotes))
print(
        f"{article_titles[max_points_index]}, "
        f"{article_upvotes[max_points_index]} points, "
        f"available at: {article_links[max_points_index]}."
)



# to check which we can scrape b\use this

#  https.//////atlast /robots.txt
