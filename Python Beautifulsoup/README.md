<div align="center">

## Python - Beautiful Soup

</div>

<div align="center">

*link: [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)*

</div>

> **IMPORTAÇÕES**

* `pip install beautifulsoup4`

> **CAPÍTULOS**

* `Beautiful Soup 4 Tutorial #1 - Web Scraping With Python`
<details>
<summary>No próprio computador</summary>

```py
from bs4 import BeautifulSoup

with open('index.html', 'r') as html_file:
    docHTML = BeautifulSoup(html_file, "html.parser")

# print(docHTML)
# MÉTODO PARA PRINTAR DE FORMA MAIS ORGANIZADA
# print(docHTML.prettify())

title_html = docHTML.title
print(title_html)
# ALTERAR O TÍTULO DO DOCUMENTO HTML
# title_html.string = "<novo título>"

text_html = docHTML.find('p')

link_html = docHTML.find_all("a")
print(link_html)
```

<summary>Scraping online</summary>

```py
import requests
from bs4 import BeautifulSoup


site_url = "https://baku-stark.github.io/Portfolio-Wallace/indexBaku.html#"

result = requests.get(site_url)
doc_HTML = BeautifulSoup(result.text, "html.parser")
# LOCALIZAR
# <ul class="nav-list mb-0 ps-0">
nav_Class = doc_HTML.find_all('ul', class_="nav-list")
print(nav_Class)
```
</details>