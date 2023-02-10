import csv

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
    
def inventrio_matriz(codigo):
    
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

def fecha_compra(codigo):

    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(row[0]==codigo):
            return fecha(row[9])
    maestra.close()
    return ""

def fecha_venta(codigo):
    
    maestra =  open (MAESTRA_PATH,"r")
    csvreader = csv.reader(maestra, delimiter=',')
    for row in csvreader:
        if(row[0]==codigo):
            return fecha(row[11])
    maestra.close()
    return ""

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
