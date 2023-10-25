import requests
from bs4 import BeautifulSoup
import json

from pprint import pprint


url = "https://spb.hh.ru/search/vacancy?text=python&area=1&area=2"

headers = {
        "user-agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Touch)"
    }


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

result = []
#заголовки
for i in soup.find_all("div", class_="serp-item"):
    link = i.find("a", class_="serp-item__title")
    cash = i.find("span", class_="bloko-header-section-2")
    company = i.find("a", class_="bloko-link bloko-link_kind-tertiary").text
    city = i.find("div", attrs={"data-qa": "vacancy-serp__vacancy-address"}).text


    if "django" in link.text.lower() or "flask" in link.text.lower():
        # print(f'{link.get("href")}, {link.text}, {cash.text}, {company}, {city}')
        result.append({
            "link": link.get("href"),
            "name": link.text,
            "cash": cash.text.replace("\u202f", ""),
            "company": company,
            "city": city
        })
    else:
        continue

pprint(result)

with open("result.json", "w", encoding="utf8") as file:
    json.dump(result, file)