import sqlite3
import os.path
from datetime import datetime


def getConexion():
    filepath = os.path.abspath("../db/dolar_diario.db")
    assert os.path.exists(filepath), "El archivo no existe | Cree en db el archivo dolar_historico.db"
    con = sqlite3.connect(filepath)
    return con


def crearBaseDolarHoy():
    con = getConexion()
    try:
        con.execute(f"""CREATE TABLE IF NOT EXISTS "dolarHoy" ("fecha" TEXT, "tipo" TEXT, "compra" TEXT, "venta" TEXT)""")
        con.commit()
        print("Base creada con exito")
    except Exception() as e:
        print(e)
    finally:
        con.close()  
        
def dropTable():
    con = getConexion()
    try:
        con.execute(f""" DROP TABLE IF EXISTS "dolarHoy" """)
        con.commit()
    except Exception() as e:
        print(e)
    finally:
        con.close()  
          

def insertarDiarios(registroDiario):

    fecha = datetime.now().date()
    con = getConexion()
    cursor = con.cursor()
    try:
        for i in range(5):
            dolar = []
            for v in registroDiario.keys():
                dolar.append(normalize(registroDiario[v][i]))
            print(dolar)
            query = f'''INSERT INTO dolarHoy(fecha, tipo, compra, venta)
                        VALUES ("{fecha}", "{dolar[0]}", {dolar[1]}, {dolar[2]} )'''
            
            print(query)
            alta = cursor.execute(query)
            con.commit()
          
    except sqlite3.Error as sqle:
        print(sqle)
    finally:
        cursor.close()
        con.close()

def deletePorFecha(fecha):
    # elimina todos los registros de una fecha 
    con = getConexion()
    try:
        con.execute(f""" DELETE FROM "dolarHoy" WHERE fecha = {fecha}""")
        con.commit()
    except Exception() as e:
        print(e)
    finally:
        con.close()  

def deletePorFecha(fecha, tipo):
    # elimina el registro con fecha y tipo especificado
    con = getConexion()
    try:
        con.execute(f""" DELETE FROM "dolarHoy" WHERE fecha = {fecha} AND tipo = {tipo}""")
        con.commit()
    except Exception() as e:
        print(e)
    finally:
        con.close() 
    
        

# para quitar los acentos (para evitar problemas con SQLite)
def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s
