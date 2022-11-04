from cgitb import html
from code import compile_command
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime


html_text = requests.get('https://dolarhoy.com/cotizacion-dolar-blue').text
soup =  BeautifulSoup(html_text, 'lxml')
dolares = soup.find_all('div', class_= 'tile is-parent is-6 is-vertical entidad')

def scraper():
    
    dolarDic = {
        
        "tipo":[],
        "compra":[],
        "venta":[]
    
    }
    
    for dolar in dolares:
        titles = dolar.find_all('div', class_="tile is-child")
        for title in titles:
                a = title.find_all('a')
                for dolar in a:
                    if dolar != []:
                    
                        p1 = dolar.find('div', class_="title")
                        p2 = dolar.find('div', class_="compra")
                        p3 = dolar.find('div', class_="venta")
                        
                        if p1 != " ":
                            dolarDic["tipo"].append(p1.get_text())
                            dolarDic["compra"].append(p2.get_text())
                            dolarDic["venta"].append(p3.get_text())
    
    fecha = datetime.now().date()
    df = pd.DataFrame(dolarDic)
    print(df)
    df.to_csv(f'../data/{fecha}-dolarHoy.csv', index=False, encoding='utf-8')

scraper()