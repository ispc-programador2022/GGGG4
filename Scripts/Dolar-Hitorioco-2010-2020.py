import requests
import pandas as pd
from bs4 import BeautifulSoup


hist_diccionary = []
variaciones_diccionary = []




# Años a consultar / solo disponibe desde 2002 hasta 2020
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]

meses = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","saptiembre","octubre","nobiembre","diciembre"]

# Cabeceras de las tablas
labels_tabla_historioco = ["Año","Mes","Compra","Venta"]



labels_tabla_variacion = ["Año","Trimestral","Semastral","Anual","Tipo"]

# Columnas historico
cols_hist = [1,3]
# Columnas variacion
cols_var = [1,3]

#Numero de filas (rows) de la tablas scrapeada.
#Mese
rows_meses = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 
#Variaciones
rows_variaciones = [16, 17, 18]



# Creo el DataFrame, historico 
df_hist = pd.DataFrame(columns=labels_tabla_historioco)
# Creo el Dataframe, variaciones
df_var = pd.DataFrame(columns=labels_tabla_variacion)
# i = 0


for year in years:  
    j = 0
    m = 0  
    
    url = f"http://www.sil1.com.ar/soft/LABORAL/CARPETA4/in7-{year}.htm"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')
    table = soup.find_all('table')
    
    # La pagian cuenta con 3 tablas, me quedo con la segunda(1)
    tabla_dolar = table[1]
      

    for row in tabla_dolar.find_all('tr'):
        if j in rows_meses:
            compra_m = row.find_all('td')[1]
            venta_m = row.find_all('td')[3]
            record_y = [year, meses[m], compra_m.get_text().strip(), venta_m.get_text().strip()]
            hist_diccionary.append(record_y)   
            m += 1
        j +=1
        
    t = 0
    varaicion_compra = [str(year)]
    varaicion_venta = [str(year)]
    for row in tabla_dolar.find_all('tr'):
        if t in rows_variaciones:
            varaicion_compra.append(row.find_all('td')[1].get_text().strip())
            varaicion_venta.append(row.find_all('td')[2].get_text().strip())
        t +=1
    varaicion_compra.append("compra")
    varaicion_venta.append("venta")
    
    variaciones_diccionary.append(varaicion_venta)    
    variaciones_diccionary.append(varaicion_compra)    


df = pd.DataFrame(hist_diccionary)
df.to_csv(f'../data/historico_dolar.csv', index=False, encoding='utf-8', header=labels_tabla_historioco)
    
df_var = pd.DataFrame(variaciones_diccionary)
df_var.to_csv(f'../data/variacion_historico_dolar.csv', index=False, encoding='utf-8', header=labels_tabla_variacion)


print("Finalizado ...")
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            # for k in e:
            #     print(k)
            #     break
                # if j in rows_meses:
                #     print(f"{f}")
                # j +=1
                
# j = 0
# for l in [2,4]:
#     for row in tabla_dolar.find_all('tr'):
#         for col in row.find_all('td')[1:3]:
#             for f in col.find("font"):
#                 if j in rows_meses:
#                     print(f"{f}")
#                 j +=1


    # print(len(col))
    # print(type(col))
    # lista = list(col)
    # for i in lista:
    #     print(i)
    #     print("------------------------------")
    # j = 1
    # for c in col:
    #     print(f"******************    {j}    ***********************")
    #     print(c)
    #     print("-----------------------------------------------------")
    #     j += 1
    # for c in col.find_all('p'):
    #     for f in c.find_all('font'):
    #         print(f)
        #  for g in c.find('font'):
        #     print(g)
        #     break

    # if(i in rows_meses):
    #     # compra= columns[1].text.strip()
    #     # venta = columns[3].text.strip()
    #     # df = df.append({'Año': years[i], 'Mes': meses[i-1],  'Compra': compra, 'Venta': venta,}, ignore_index=True)
    #     # print(f"{columns[0].get_text()}")
        
    # # if(i in rows_variaciones):
    # #     ...
    # i+=1
        # print(df)