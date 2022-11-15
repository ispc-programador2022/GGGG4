from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime

import dml_dolar_hoy

def scraper():
    
    html_text = requests.get('https://dolarhoy.com/cotizacion-dolar-blue').text
    soup =  BeautifulSoup(html_text, 'lxml')
    
    """
    Estructura del documento HTML

    En alguna parte:
    
    
    <div> con clase "tile is-parent is-6 is-vertical entidad"
        |_ <div> con clase "tile is-child"
            |_ <a> "links"
                |_ <div> con clase "title"
                |_ <div> con clase "compra"
                |_ <div> con clase "venta"
    """
    
    
    # Me quedo con los divs que tienen la clase "tile is-parent is-6 is-vertical entidad"
    dolares = soup.find_all('div', class_= 'tile is-parent is-6 is-vertical entidad')
    
    
    dolarDic = {
        
        "tipo":[],
        "compra":[],
        "venta":[]
    
    }
    
    
    for dolar in dolares:
        # Me quedo con los divs con la clase tile is-child
        titles = dolar.find_all('div', class_="tile is-child")
        for title in titles:
                # Me quedo con los los elementos de tipo a "links"
                a = title.find_all('a')
                for dolar in a:
                    if dolar != []:
                        # Dentro de cada elemento a ahy elementos divs con los datos de cada tipo de dolar 
                        # El nombre del tipo de dolar, el valor para la compra y el de vetnta
                        p1 = dolar.find('div', class_="title")
                        p2 = dolar.find('div', class_="compra")
                        p3 = dolar.find('div', class_="venta")
                        
                        if p1 != " ":
                            #Los agrego al diccionario
                            dolarDic["tipo"].append(p1.get_text())
                            dolarDic["compra"].append(p2.get_text())
                            dolarDic["venta"].append(p3.get_text())
    
    fecha = datetime.now().date()
    dml_dolar_hoy.insertarDiarios(dolarDic)
    df = pd.DataFrame(dolarDic)
    df.to_csv(f'../data/diario/{fecha}-dolarHoy.csv', index=False, encoding='utf-8')
    return df