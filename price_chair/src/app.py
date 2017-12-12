author = "yuri"

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/Imarku-Kitchen-Stainless-Ergonomic-Equipment/dp/B01DDBJF12/ref=sr_1_2?m=A18PWGWM4BW1FI&s=merchant-items&ie=UTF8&qid=1512835293&sr=1-2&keywords=B01GHNMGIC%7CB01DDBJF12%7CB071CZ47G8")

content = request.content
soup = BeautifulSoup(content, "html.parser")
element = soup.find("span", {"id": "priceblock_dealprice", "class": "a-size-medium a-color-price"})

string_element = element.text.strip()
string_element_without_symbol = string_element[1:]

price = float(string_element_without_symbol)

if price < 20:
    print("Buy the chair.")
    print("The price is {}".format(string_element))
else:
    print("Don't buy the chair.")