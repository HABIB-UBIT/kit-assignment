import requests
from bs4 import BeautifulSoup
import csv

res = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
text= res.text
status_code= res.status_code
# print(status_code , text)
soup = BeautifulSoup(res.content, 'html.parser')
page_title= soup.title.text
page_body= soup.body
page_head= soup.head.text
# print(f'page_title ------->', page_title)
# print(f'page_body ------->', page_body)
# print(f'page_head ------->', page_head)
all_h1_tags = []
all_p_tag = []
top_items = []
# for element in soup.select('h1'):
#     all_h1_tags.append(element.text)
# print(f'headings ------->' , all_h1_tags)
# for elements in soup.select('p'):
#     all_p_tag.append(elements.text)
# print(f'paragraphs ------->' , all_p_tag[6])
for element in soup.select('a.title'):
    top_items.append(element.text)
# print(top_items)
products = soup.select('div.thumbnail')
for elem in products:
    title = elem.select('h4 > a.title')[0].text
    review_label = elem.select('div.ratings')[0].text
    info = {
        "title": title.strip(),
        "review": review_label.strip()
    }
    top_items.append(info)

# print(top_items)

all_links= []
links= soup.select('a')
for ahref in links:
    text = ahref.text 
    href = ahref.get('href')
    all_links.append({"href": href, "text": text})
# print(all_links)
all_products = []

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)