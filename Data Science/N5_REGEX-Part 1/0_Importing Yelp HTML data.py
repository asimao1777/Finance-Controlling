import requests
from bs4 import BeautifulSoup
import pprint
import re


url = "https://cse6040.gatech.edu/datasets/yelp-example/"


with open(r, "r", encoding="utf-8") as yelp_file:
    yelp_html = yelp_file.read()

soup = BeautifulSoup(yelp_html, "html.parser")

pr = []
rankings = []
names = []
stars = []
reviews = []
prices = []

for name in soup.find_all("a", class_="biz-name js-analytics-click"):
    print(name)
    names.append(str(name.span.get_text()))

for star in soup.find_all("img", class_="offscreen"):
    star_num = star.get("alt")
    print(star_num)
    fs = str(star_num)
    stars.append(fs[:3])

for rev in soup.find_all("span", class_="review-count rating-qualifier"):
    rev = rev.get_text()
    rev_num = rev.strip()
    cl = re.compile("[0-9]+")
    reviews.append(int(cl.search(rev_num).group()))

for price in soup.find_all("span", class_="business-attribute price-range"):
    price = price.get_text()
    prices.append(price.strip())

# print(names)
# print(stars)
# print(reviews)
# print(prices)

for i in range(len(names)):
    rankings.append(
        {"name": names[i], "stars": stars[i], "numrevs": reviews[i], "price": prices[i]}
    )

rankings = rankings[2:12]

pprint.pprint(rankings)
