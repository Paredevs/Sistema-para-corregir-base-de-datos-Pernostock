#Funciones para obtener datos de las sucursales
import csv,time

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
    