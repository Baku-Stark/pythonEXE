import requests
from bs4 import BeautifulSoup


site_url = "https://baku-stark.github.io/Portfolio-Wallace/indexBaku.html#"

result = requests.get(site_url)
doc_HTML = BeautifulSoup(result.text, "html.parser")
# LOCALIZAR
# <ul class="nav-list mb-0 ps-0">
nav_Class = doc_HTML.find_all('ul', class_="nav-list")
print(nav_Class)