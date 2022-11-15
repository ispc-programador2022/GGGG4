import sqlite3
import os.path
import pandas as pd


filepath = os.path.abspath("../db/dolar_historico.db")
assert os.path.exists(filepath), "El archivo no existe | Cree en db el archivo dolar_historico.db"
con = sqlite3.connect(filepath)

con.execute("DELETE FROM historico")
df = pd.read_csv("../data/historico_dolar.csv")
df.to_sql("historico", con, if_exists='append', index=False)


con.execute("DELETE FROM variaciones")
df = pd.read_csv("../data/variacion_historico_dolar.csv")
df.to_sql("variaciones", con, if_exists='append', index=False)
