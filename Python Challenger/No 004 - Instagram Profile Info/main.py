# importing libraries
import requests
from bs4 import BeautifulSoup


# Função personalizada
from profilepic import pp_download

def banner():
    instagram = """
         __  .__   __.      _______..___________.     ___        _______ .______           ___      .___  ___. 
        |  | |  \ |  |     /       ||           |    /   \      /  _____||   _  \         /   \     |   \/   | 
        |  | |   \|  |    |   (----``---|  |----`   /  ^  \    |  |  __  |  |_)  |       /  ^  \    |  \  /  | 
        |  | |  . `  |     \   \        |  |       /  /_\  \   |  | |_ | |      /       /  /_\  \   |  |\/|  | 
        |  | |  |\   | .----)   |       |  |      /  _____  \  |  |__| | |  |\  \----. /  _____  \  |  |  |  | 
        |__| |__| \__| |_______/        |__|     /__/     \__\  \______| | _| `._____|/__/     \__\ |__|  |__|
        \n
         __  .__   __.  _______   ______   
        |  | |  \ |  | |   ____| /  __  \  
        |  | |   \|  | |  |__   |  |  |  | 
        |  | |  . `  | |   __|  |  |  |  | 
        |  | |  |\   | |  |     |  `--'  | 
        |__| |__| \__| |__|      \______/  
    """
    return print(instagram)

# instagram URL
URL = "https://www.instagram.com/{}/"
 
# parse function
def parse_data(s):
     
    # creating a dictionary
    data = {}
     
    # splitting the content
    # then taking the first part
    s = s.split("-")[0]
     
    # again splitting the content
    s = s.split(" ")
     
    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
     
    # returning the dictionary
    return data
 
# scrape function
def scrape_data(username):
     
    # getting the request from url
    r = requests.get(URL.format(username))
     
    # converting the text
    s = BeautifulSoup(r.text, "html.parser")
     
    # finding meta info
    meta = s.find("meta", property ="og:description")
     
    # calling parse method
    return parse_data(meta.attrs['content'])
 
# main function
if __name__=="__main__":
     
    # nome do usuário
    username = str(input("Digite o nome do usuário\nr: "))
     
    # calling scrape function
    data = scrape_data(username)
     
    # mostrar toda a informação obtida
    banner()
    print('-'*120)
    print(f"Seguidores: {data['Followers']}\nSeguindo: {data['Following']}\nQtd de Posts: {data['Posts']}")
    pp_download(username)