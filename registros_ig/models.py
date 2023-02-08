from registros_ig.conexion import Conexion
import requests
from config import apikey


def cambios(value_from, value_to):
    r=requests.get(f'http://rest.coinapi.io/v1/exchangerate/{value_from}/{value_to}?apikey={apikey}')
    resultado=r.json()
  
    return resultado["rate"]


def select_all():
    connet=Conexion("SELECT id,date,hora,Moneda_from,Cantidad_from,Moneda_to, cantidad_to FROM criptos order by date;")
    
    filas = connet.cur.fetchall()#capturo las filas de datos
    columnas = connet.res.description#capturo los nombres de columnas
    
    resultado = []#lista para guardar diccionario
     
    for fila in filas:
        dato = {}#diccionario para cada registro
        posicion = 0#posicion columna
        
        for campo in columnas:
            dato[campo[0]]=fila[posicion]
            posicion += 1
        resultado.append(dato)
        
    connet.con.close()   
    
    return resultado



def insert(registro):
    connetInsert=Conexion("insert into criptos(date,hora,Moneda_from,Cantidad_from,Moneda_to, cantidad_to) values(?,?,?,?,?,?)",registro)
    
    connetInsert.con.commit()#funcion que registra finalmente
    
    connetInsert.con.close()
    
    
    
    
    
    
    
def select_by(id):
   
    connetSelectBy = Conexion(f"SELECT id,date,hora,Moneda_from,Cantidad_from,Moneda_to, cantidad_to FROM criptos WHERE id={id}")
    resultado=connetSelectBy.res.fetchall()
    connetSelectBy.con.close()
    return resultado[0]
    

def delete_by(id):    
    connetDeleteby = Conexion(f"DELETE FROM criptos WHERE id={id}")
    
    connetDeleteby.con.commit()
    connetDeleteby.con.close()
    
def update_by(id,registro):
    connectUpdate=Conexion(f"UPDATE criptos SET date=?,hora=?,Moneda_from=?,Cantidad_from=?,Moneda_to=?, cantidad_to=? WHERE id={id}",registro)
    connectUpdate.con.commit()
    connectUpdate.con.close()