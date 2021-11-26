from bs4 import BeautifulSoup
import requests
import csv

data = {}
out_filename = "enseignants.csv"
headers = "enseignant; profession \n"
f = open(out_filename, "wt+",encoding='utf8')
f.write(headers)

page_url = "http://www.fsgf.rnu.tn/fra/enseignants"
uClient = requests.get(page_url)
page_soup = BeautifulSoup(uClient.content, "html.parser")

uClient.close()
containers = page_soup.findAll("div", {"class": "tcard-content-item"})

for idx,container in enumerate(containers):
    
    enseignant = container.find("div",{"class":"h2"}).text.strip()
    profession = container.find("div",{"class":"h3"}).text.strip()
    
    print("Enseignant : ", enseignant, ", Profession :  ", profession)
    f.write(enseignant + ";" + profession +"\n")  
f.close() 

print(idx)
import pandas as pd 
data = pd.read_csv("enseignants.csv" , encoding='utf-8',delimiter=';')


data.head()