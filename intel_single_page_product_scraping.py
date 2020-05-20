from bs4 import BeautifulSoup
import requests
html = requests.get(
    "https://www.intel.com/content/www/us/en/products/processors/core/x-series.html").text
view = BeautifulSoup(html, 'lxml')

for items in view.find_all(class_='item-wrap1'):

    try:
        item_link = items.a
    except Exception as e:
        item_link = None
    print(f"Item Link : https://www.intel.com{item_link['href']}")

    try:
        item_title = items.h3.text.strip()
    except Exception as e:
        item_title = None
    print(f"Item Titel : {item_title}")

    try:
        item_info = items.find(class_='card-info')
    except Exception as e:
        item_info = None
    ul = item_info.find('ul')
    for li in ul.find_all('li'):
        print(f"Item info : {li.text.strip()}")

    print("XXXX-------XXX------XXXX")
