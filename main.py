import pandas as pd
import requests
from bs4 import BeautifulSoup

url = ""
r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

# Extract product names
names = soup.find_all("a", class_="title")
product_name = []

for i in names:
    name = i.text.strip()
    product_name.append(name)

# print("Product Names:", product_name)

# Extract product prices
prices = soup.find_all("h4", class_="price float-end card-title pull-right")
prices_list = []

for j in prices:
    price = j.text.strip()
    prices_list.append(price)

# print("Prices:", prices_list)

#Extract product description

desc = soup.find_all("p", class_="description")
desc_list = []
for i in desc:
    des = i.text
    desc_list.append(des)

# print("Descriptions:", desc_list)

reviews = soup.find_all("p", class_="review-count float-end")
reviews_list = []
for j in reviews:
    review = j.text.strip()
    reviews_list.append(review)
# print("Reviews:", reviews_list)

data = {
    "product_name": product_name,
    "product_price": prices_list,
    "product_description": desc_list,
    "reviews": reviews_list
}

df = pd.DataFrame(data)
# print(df)

df.to_excel("products.xlsx", index=False)
