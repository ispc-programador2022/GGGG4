# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 20:05:09 2022

@author: pedro
"""

import requests
import csv
from bs4 import BeautifulSoup


page = requests.get("https://www.cronista.com/MercadosOnline/monedas.html").text
soup = BeautifulSoup(page, "lxml")

nombres_monedas=soup.find_all("span",class_="name")
compra=soup.find_all("span", class_="value")
venta=soup.find_all("span")


nombre_moneda=soup.find("a",class_="span")

lista_nombres=list(nombres_monedas)
nombres=[]
cont=0
for i in lista_nombres:
    nombres.append(str(i))
    cont+=1
    if cont==3:
        break

for moneda in nombres:
    for letra in moneda:
        if letra.isupper()==True:
            print("MA")
    
       

    
print(nombres)
type(nombres[0])
#filtrar el resultado ese
