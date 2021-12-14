import requests
from  bs4 import BeautifulSoup 
from requests.api import request
req = input('Enter the request: ')
references = []

def split(str):
     res = str[7:]
     res = res.split('&', 1)[0]
     return res
def out(h3,ref,page):
     traits = ""
     for i in range(1,150):
          traits+="-"
     res = traits+ '\n\n\t'+ str(h3.find("div").text) +'\n\n\t\t' +split(ref) + '\n\n\t\t' + 'Page: ' + str(int(page/10 + 1))
     return res
pages = [0,10]
for page in pages:
     url = f"https://www.google.com/search?q={req}&start={page}"
     response = requests.get(url)
     soup = BeautifulSoup(response.text, "html.parser")
     h3s = soup.find_all('h3')
     for h3 in h3s:
          references.append(h3.parent)
          ref = str(h3.parent.get("href"))
          if(ref!='None'):
               print(out(h3,ref,page))
