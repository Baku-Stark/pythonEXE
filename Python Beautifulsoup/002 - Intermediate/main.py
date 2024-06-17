import requests
from bs4 import BeautifulSoup

class BS4_Scrapping:
    def __init__(self, url : str) -> None:
        req = requests.get(url)

        if req.status_code == 200:
            #print(req.text)
            
            # prettify() -> deixar o html estilizado
            req_html = BeautifulSoup(req.text, "html.parser")
            print(f"=== [ {req_html.title.string} ] ===")
            print(req_html.prettify())

        else:
            print(f"{__class__.__name__} [{req.status_code}] : ERROR STATUS")

if __name__ == '__main__':
    BS4_Scrapping("https://www.bing.com/search?pc=MOZI&form=MOZLBR&q=teste+")