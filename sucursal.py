#Funciones para obtener datos de las sucursales
import csv,time,operator
import itertools
from collections import Counter
from tqdm import tqdm

MAESTRA_PATH = "./database/maestra 8-2-23.csv"
BODEGA_PATH = "./database/bodega.csv"
MATRIZ_PATH = "./database/matriz.csv"
LASERENA_PATH = "./database/la serena.csv"
INDUSTRIAL_PATH = "./database/barrio_industrial.csv"

def recorre_maestra():
    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        return row
    maestra.close()

def inventario_bodega(codigo):

    bodega =  open (BODEGA_PATH,"r")
    csvreader = csv.reader(bodega, delimiter=',')
    inicio = 0
    
    for row in csvreader:
        
        if(inicio==3):
            if(codigo == row[0]):
                return row[5]
                
        else:
            
            inicio = inicio + 1
    bodega.close()
    return ""
    
def inventario_matriz(codigo):
    
    matriz =  open (MATRIZ_PATH,"r")
    csvreader = csv.reader(matriz, delimiter=',')
    inicio = 0
    
    for row in csvreader:
        
        if(inicio==3):
            if(codigo == row[0]):
                return row[5]
                
        else:
            
            inicio = inicio + 1
    matriz.close()
    return ""

def inventario_laserena(codigo):
    
    laserena =  open (LASERENA_PATH,"r")
    csvreader = csv.reader(laserena, delimiter=',')
    inicio = 0
    
    for row in csvreader:
        
        if(inicio==3):
            if(codigo == row[0]):
                return row[5]
                
        else:
            
            inicio = inicio + 1
    laserena.close()
    return ""

def inventario_industrial(codigo):

    
    industrial =  open (INDUSTRIAL_PATH,"r")
    csvreader = csv.reader(industrial, delimiter=',')
    inicio = 0
    
    for row in csvreader:
        
        if(inicio==3):
            if(codigo == row[0]):
                return row[5]
                
        else:
            
            inicio = inicio + 1
    industrial.close()
    return ""

def fecha_compra_venta(codigo):

    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(row[0]==codigo):
            return fecha(row[9]),fecha(row[11])
    maestra.close()
    return "",""


def fecha(fecha):
    
    if(fecha == None or fecha == "" or fecha.isspace()):
        return ""
    else:
        dia = fecha[0:2]
        mes = fecha[2:4]
        anio = fecha[4:8]
       # print(dia,"/",mes,"/",anio)
        #time.sleep(1)
    return dia + "/" + mes + "/" + anio


def guarda_inventario_matriz():

    matriz =  open (MATRIZ_PATH,"r")
    csvreader = csv.reader(matriz, delimiter=',')
    inicio = 0
    inventario = {}
    
    for row in csvreader:
        if(inicio==3):
            
            inventario[row[0]]=row[5]

            
        else:
            inicio = inicio + 1
    matriz.close()
    return inventario

def guarda_inventario_bodega():
    
        bodega =  open (BODEGA_PATH,"r")
        csvreader = csv.reader(bodega, delimiter=',')
        inicio = 0
        inventario = {}
        for row in csvreader:
            if(inicio==3):
                inventario[row[0]]=row[5]
            else:
                inicio = inicio + 1
        bodega.close()
        return inventario

def guarda_inventario_laserena():
        
            inventario = {}
            laserena =  open (LASERENA_PATH,"r")
            csvreader = csv.reader(laserena, delimiter=',')
            inicio = 0
            for row in csvreader:
                if(inicio==3):
                    
                    inventario[row[0]]=row[5]
                else:
                    inicio = inicio + 1
            laserena.close()
            return inventario

def guarda_inventario_industrial():
            
                inventario = {}
                industrial =  open (INDUSTRIAL_PATH,"r")
                csvreader = csv.reader(industrial, delimiter=',')
                inicio = 0
                for row in csvreader:
                    if(inicio==3):
                        
                        inventario[row[0]]=row[5]
                    else:
                        inicio = inicio + 1
                industrial.close()
                return inventario

def guarda_fechas_compra_venta():

    fecha = {}
    
    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
           
            fecha.setdefault(row[0], [])
            fecha[row[0]].append(row[9])
            fecha[row[0]].append(row[11])
           
            
    maestra.close()
    
    return fecha
    
def buscaDuplicadoDict(key_original,value,dict):
    for key in dict:
        
        if(key!=key_original):
            # print("key:",key,"key_original:",key_original)
            # time.sleep(1)
            if(dict[key]==value):
                #print("key:",key,"key_original:",key_original)
                return True
    #print("key:",key)
    return False
def duplicadosExactos(DB_PATH):
    
    data = []
    des_dict = {}
    descripciones = []
    descripciones_duplicadas =[]
    base_datos = open(DB_PATH,'r')
    csvreader = csv.reader(base_datos,delimiter=',')
    lista_desc_duplicadas = {}
    for row in csvreader:
        #print(len(row))
        if(len(row)>1):
            if(row[0][0].isdigit()):
            #print("row:",row)
            #input()
                # data.append(row[1].strip())
                des_dict[row[0]] = row[1].strip()
            
            #lista_desc_duplicadas[row[0]]= descripcion_actual
                # codigo_actual = row[0]
                # lista_desc_duplicadas[codigo_actual].append(descripciones_duplicadas.index(descripcion_actual))
    base_datos.close()
    print("Cantidad de productos con duplicados: ",len(descripciones_duplicadas))
    for key in tqdm(list(des_dict)):

        # print(key, '->', des_dict[key])
        # time.sleep(1)
        if(buscaDuplicadoDict(key,des_dict[key],des_dict) == False):
            del des_dict[key]
            
    
    #print(des_dict)
    # for key in des_dict:
        
    #     print(key, '->', des_dict[key])
       # time.sleep(1)
    
    # duplicates = {k for k, v in Counter(data).items() if v > 1}
    # result = [el for el in data if el in duplicates]
    # print(result)
# [1, 3, 1, 2, 3, 5, 1, 5, 2]
    # print(lista_desc_duplicadas)
    duplicados = set(des_dict.values())
    d = {}
    for n in duplicados:
        d[n] = [k for k in des_dict.keys() if des_dict[k] == n]
    print(d)
    print("Cantidad de productos con duplicados: ",len(d))

    # for i in descripciones_duplicadas:
    #     print(i)
