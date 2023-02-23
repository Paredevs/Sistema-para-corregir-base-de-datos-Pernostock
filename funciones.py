#Funciones para obtener datos de las sucursales y Maestra
import csv,time,operator,re,os
import itertools
from collections import Counter
from tqdm import tqdm
from pathlib import Path

#Path de los archivos
MAESTRA_PATH = "./database/Maestra.csv"
BODEGA_PATH = "./database/Bodega central.csv"
MATRIZ_PATH = "./database/Casa matriz.csv"
LASERENA_PATH = "./database/La Serena.csv"
INDUSTRIAL_PATH = "./database/Barrio industrial.csv"
RESULTS_PATH = "./resultados/" #Path de los resultados


def compruebaBasededatos():  #Verifica si existen las bases de datos

    maestra = Path(MAESTRA_PATH)
    bodega = Path(BODEGA_PATH)
    matriz = Path(MATRIZ_PATH)
    laserena = Path(LASERENA_PATH)
    industrial = Path(INDUSTRIAL_PATH)

    maestra_file =False
    bodega_file = False
    matriz_file = False
    laserena_file = False
    industrial_file = False

    bases_que_faltan = 'Faltan los siguientes archivos en la carpeta '+RESULTS_PATH+' o estan mal escritos:\n'
    
    if (maestra.is_file() and bodega.is_file() and matriz.is_file() and laserena.is_file() and industrial.is_file()):
        return True
    else:
        if(not maestra.is_file()):
            bases_que_faltan += '-Maestra.csv\n'
        if(not bodega.is_file()):
            bases_que_faltan += '-Bodega central.csv\n'
        if(not matriz.is_file()):
            bases_que_faltan += '-Casa matriz.csv\n'
        if(not laserena.is_file()):
            bases_que_faltan += '-La Serena.csv\n'
        if(not industrial.is_file()):
            bases_que_faltan += '-Barrio industrial.csv\n'
    return bases_que_faltan

            
    return False

def recorre_maestra():

    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        return row
    maestra.close()

def esCodigo(codigo):
    if(len(codigo)>1):
            if(codigo[0][0].isdigit()):
                return True
    return False

def getInventarioBodega(codigo):

    bodega =  open (BODEGA_PATH,"r")
    csvreader = csv.reader(bodega, delimiter=',')
    for row in csvreader:
        
        if(esCodigo(row)):
            if(codigo == row[0]):
                return row[5]  
    bodega.close()
    return ""
    
def getInventarioMatriz(codigo):
    
    matriz =  open (MATRIZ_PATH,"r")
    csvreader = csv.reader(matriz, delimiter=',')
    
    for row in csvreader:
        if(esCodigo(row)):
            if(codigo == row[0]):
                return row[5]
    matriz.close()
    return ""

def getInventarioLaserena(codigo):
    
    laserena =  open (LASERENA_PATH,"r")
    csvreader = csv.reader(laserena, delimiter=',')
    
    for row in csvreader:
        
        if(esCodigo(row)):
            if(codigo == row[0]):
                return row[5]
    laserena.close()
    return ""

def getInventarioIndustrial(codigo):

    
    industrial =  open (INDUSTRIAL_PATH,"r")
    csvreader = csv.reader(industrial, delimiter=',')
    
    for row in csvreader:
        
       if(esCodigo(row)):
            if(codigo == row[0]):
                return row[5]
    industrial.close()
    return ""

def getFechacompraventaMaestra(codigo):

    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(row[0]==codigo):
            return setFecha(row[9]),setFecha(row[11])
    maestra.close()
    return "",""

def getFechacompraventabodega(codigo):
    bodega = open (BODEGA_PATH,"r")
    csvreader = csv.reader(bodega,delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            if(row[0]==codigo):
                
                return setFechasucursal(row[20]),setFechasucursal(row[22])
    bodega.close()
    return "",""

def getFechacompraventamatriz(codigo):
    matriz = open (MATRIZ_PATH,"r")
    csvreader = csv.reader(matriz,delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            if(row[0]==codigo):
                return setFechasucursal(row[20]),setFechasucursal(row[22])
    matriz.close()
    return "",""
    
def getFechacompraventalaserena(codigo):
    laserena = open (LASERENA_PATH,"r")
    csvreader = csv.reader(laserena,delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            if(row[0]==codigo):
                return setFechasucursal(row[20]),setFechasucursal(row[22])
    laserena.close()
    return "",""

def getFechacompraventaindustrial(codigo):

    industrial = open (INDUSTRIAL_PATH,"r")
    csvreader = csv.reader(industrial,delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            if(row[0]==codigo):
                return setFechasucursal(row[20]),setFechasucursal(row[22])
    industrial.close()
    return "",""


def setFecha(fecha):
    
    if(fecha == None or fecha == "" or fecha.isspace()):
        return ""
    else:
        dia = fecha[0:2]
        mes = fecha[2:4]
        anio = fecha[4:8]
      
    return dia + "/" + mes + "/" + anio

def setFechasucursal(fecha):
    
    if(fecha == None or fecha == "" or fecha.isspace()):
        return ""
    else:
        anio = fecha[0:4]
        mes = fecha[4:6]
        dia = fecha[6:8]
    return dia + "/" + mes + "/" + anio


def guarda_inventario_matriz():

    matriz =  open (MATRIZ_PATH,"r",encoding = 'unicode_escape')
    csvreader = csv.reader(matriz, delimiter=',')
    inventario = {}
    for row in csvreader:
        if(esCodigo(row)):
            inventario[row[0]]=row[5]
    matriz.close()
    return inventario

def guarda_inventario_bodega():
    
        bodega =  open (BODEGA_PATH,"r",encoding = 'unicode_escape')
        csvreader = csv.reader(bodega, delimiter=',')
        inventario = {}
        for row in csvreader:
            if(esCodigo(row)):
                inventario[row[0]]=row[5]
        bodega.close()
        return inventario

def guarda_inventario_laserena():
        
            inventario = {}
            laserena =  open (LASERENA_PATH,"r",encoding = 'unicode_escape')
            csvreader = csv.reader(laserena, delimiter=',')
            for row in csvreader:
                if(esCodigo(row)):
                    inventario[row[0]]=row[5]
            laserena.close()
            return inventario

def guarda_inventario_industrial():
            
                inventario = {}
                industrial =  open (INDUSTRIAL_PATH,"r",encoding = 'unicode_escape')
                csvreader = csv.reader(industrial, delimiter=',')
                for row in csvreader:
                    if(esCodigo(row)):
                        inventario[row[0]]=row[5]
                industrial.close()
                return inventario

def guarda_fechas_compra_venta():

    fecha = {}
    
    maestra =  open (MAESTRA_PATH,"r",encoding = 'unicode_escape')
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
            if(dict[key]==value): #Si la descripcion actual es igual a la de otro producto se mantienen ambos
                return True
    return False #Si la descripcion no es igual a la de otro producto se elimina

def duplicadosExactosAgrupados(DB_PATH,i_descripcion): #Funcion encargada de buscar los productos con descripciones exactas y agruparlos en un diccionario
    
    descripciones_duplicadas = {}    
    base_datos = open(DB_PATH,'r',encoding = 'unicode_escape') #Se abre la base de datos, dependiendo de ubicacion
    csvreader = csv.reader(base_datos,delimiter=',')

    for row in csvreader: #Se recorre la base de datos
        if(esCodigo(row)): #Se verifica que la fila tenga codigo
            if(len(row)>1):
                if(row[0][0].isdigit()):
                    descripciones_duplicadas[row[0]] = row[i_descripcion].strip()  #Se quitan los espacios en blanco al inicio/final de la descripcion

    base_datos.close() 

    for key in tqdm(list(descripciones_duplicadas)): #Se recorre el diccionario de descripciones
        if(buscaDuplicadoDict(key,descripciones_duplicadas[key],descripciones_duplicadas) == False):  #Si el producto no tiene duplicados se elimina
            del descripciones_duplicadas[key]
            
    duplicados = set(descripciones_duplicadas.values())
    dic_duplicados = {}
    for n in duplicados:
        dic_duplicados[n] = [k for k in descripciones_duplicadas.keys() if descripciones_duplicadas[k] == n] #Agrupa los productos que tienen la misma descripcion en un diccionario, la llave es la descripcion y el valor es una lista con los codigos de los productos que tienen esa descripcion
    return dic_duplicados

def descripciones_sinsentido(descripcion): #Funcion encargada de buscar las descripciones que no tienen sentido o son erroneas
   
    x = re.findall("[{}¿?]|ÑT|EMBRAGE|UUU|ISQ|AAAA|BBB|CCCC|EEE|HHKG|LLLL|(^PP5|^PP\d$|PPP\d$|PPPP$)|QQQ|RRRR|LALVE|SSS|^XXX|INMIVI|MAUSE|^MASA|(PARACHOQ|PARACH|PARACHOE|PARACHO)$|([^a-zA-Z]PARACH[^a-zA-Z])|5NJ|DSIC|DSIT|SDF|SASD|YYY|^LB$|VACA|DI9S|^A$|^H$|PEDIDO|DIDP|DIS`|GRT|NWU|80X40X15X3MM", descripcion)
    #x = re.findall("^CORREA \dPK.*|(^CORREA V.* \dPK \d\d\d\d)",descripcion)
    #x = re.findall("PEDIDOS",descripcion)
    if(x):
        #print(" D:",descripcion)
        
        return True

    #AAAA|BBB|CCCC
    # if(x):
    #     pass
    #     print("B o V: ",row[0]," D:",descripcion)
    # x = re.search('(TAMOR|V)', descripcion)
    # if(x):
        
    #    # print("TAM*OR: ",row[0]," D:",descripcion)
    #     return 1
    return False

def verificaCarpeta():  #Funcion encargada de verificar si existe la carpeta de resultados, si no existe la crea
    newpath = r''+RESULTS_PATH 
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def getFamilia(descripcion):  #Funcion encargada de obtener la familia de un producto a partir de su descripcion
    maestra = open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            if(row[1].strip()==descripcion):
                return row[4]
    maestra.close()
    return ""

def getSubgrupo(descripcion):   #Funcion encargada de obtener el subgrupo de un producto a partir de su descripcion
    maestra = open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(row[1].strip()==descripcion):
            return row[5]
    maestra.close()
    return ""

def getStock():    #Funcion encargada de obtener el stock de todas las sucurales, y retornarlos en un diccionario


    stock_matriz,stock_bodega,stock_laserena,stock_industrial = {},{},{},{}

    maestra = open (MAESTRA_PATH,"r",encoding = 'unicode_escape')
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
                if(row[14]!=""):
                    stock_matriz[row[0]] = str(row[14])
                   # print("stock matriz: ",stock_matriz)
                else:
                    stock_matriz[row[0]] = ""
                if(row[15]!=""):
                    stock_laserena[row[0]] = str(row[15])
                    #print("stock laserena: ",stock_laserena)
                else:
                    stock_laserena[row[0]] = ("")
                if(row[16]!=""):
                    stock_industrial[row[0]] = str(row[16])
                   # print("stock industrial: ",stock_industrial)
                else:
                    stock_industrial[row[0]] = ""
                if(row[17]!=""):
                    stock_bodega[row[0]] = str(row[17])
                    #print("stock bodega: ",stock_bodega)
                else:
                    stock_bodega[row[0]] = ""
                #print(row[0],stock_matriz,stock_laserena,stock_industrial,stock_bodega)
    maestra.close()
    return stock_matriz,stock_laserena,stock_industrial,stock_bodega


def getCompra():

    compra = {}
    maestra = open (MAESTRA_PATH,"r",encoding = 'unicode_escape')
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            compra[row[0]] = setFecha(row[9])
    maestra.close()
    return compra
     
def getVenta():

    venta = {}
    maestra = open (MAESTRA_PATH,"r",encoding = 'unicode_escape')
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(esCodigo(row)):
            venta[row[0]] = setFecha(row[11])
    maestra.close()
    return venta

