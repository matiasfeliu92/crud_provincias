import requests
from bs4 import BeautifulSoup

def scrapping():
    url = "https://cdn.educ.ar/dinamico/UnidadHtml__get__c9da45fe-4b48-11e1-82ba-ed15e3c494af/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    name = soup.find_all('strong')
    names = [n.string for n in name]
    print(names)
    # for n in name:
    #     print(n.string)

scrapping()