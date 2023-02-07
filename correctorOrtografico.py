import csv,time,pandas,numpy as np
from tabulate import tabulate
import re



from tqdm import tqdm



    
def inventariado_industrial(codigo):

    codigo = int(codigo)
    inicio = 0
   
    if(codigo in codigos_industrial):
        
     #   input("Se encontro el codigo en bodega")
        return inv_industrial[codigos_industrial.index(codigo)]
    return ""

def inventariado_laserena(codigo):

    codigo = int(codigo)
    inicio = 0
   
    if(codigo in codigos_laserena):
        
     #   input("Se encontro el codigo en bodega")
        return inv_laserena[codigos_laserena.index(codigo)]
    return ""

def inventariado_matriz(codigo):

    codigo = int(codigo)
    inicio = 0
   
    if(codigo in codigos_matriz):
        
        #input("Se encontro el codigo en matriz")
        return inv_matriz[codigos_matriz.index(codigo)]
    return "" 

def inventariado_bodega(codigo):


    codigo = int(codigo)
    inicio = 0
   
    if(codigo in codigos_bodega):
        
    #    input("Se encontro el codigo en bodega")
        return inv_bodega[codigos_bodega.index(codigo)]
   # bodega = open ("./database/bodega.csv","r")
   # csvreader = csv.reader(bodega, delimiter=',')
   # for row in csvreader:
    #    if(inicio==3):
            # codigo_sucursal = int(row[0].replace(" ",""))
           # if(codigo_sucursal==(codigo)):
            #    return row[5]
     #   else:
      #     inicio = inicio + 1
    
  #  bodega.close()

    
    return "" 


def guarda_codigos():


    inicio = 0
    bodega = open ("./database/bodega.csv","r")
    csvreader = csv.reader(bodega, delimiter=',')
    for row in csvreader:
        if(inicio==3):
            codigo_sucursal = int(row[0].replace(" ",""))
            codigos_bodega.append(codigo_sucursal)
            inv_bodega.append(row[5])
           
        else:
           inicio = inicio + 1
    bodega.close()

    inicio = 0
    laserena = open ("./database/la serena.csv","r")
    csvreader = csv.reader(laserena, delimiter=',')
    for row in csvreader:
        if(inicio==3):
            codigo_sucursal = int(row[0].replace(" ",""))
            codigos_laserena.append(codigo_sucursal)
            inv_laserena.append(row[5])
           
        else:
           inicio = inicio + 1
    laserena.close()

    inicio = 0
    industrial = open ("./database/barrio_industrial.csv","r")
    csvreader = csv.reader(industrial, delimiter=',')
    for row in csvreader:
        if(inicio==3):
            codigo_sucursal = int(row[0].replace(" ",""))
            codigos_industrial.append(codigo_sucursal)
            inv_industrial.append(row[5])
           

        else:
           inicio = inicio + 1
    industrial.close()

    
    inicio = 0
    matriz = open ("./database/matriz.csv","r")
    csvreader = csv.reader(matriz, delimiter=',')
    for row in csvreader:
        if(inicio==3):
            codigo_sucursal = int(row[0].replace(" ",""))
            codigos_matriz.append(codigo_sucursal)
            inv_matriz.append(row[5])
        
                
        else:
           inicio = inicio + 1
    
    matriz.close()


def fecha(fecha):
    if(fecha == None or fecha == "" or fecha.isspace()):
        return ""
    else:
        dia = fecha[0:2]
        mes = fecha[3:5]
        anio = fecha[6:10]
    return anio + "/" + mes + "/" + dia

def errores_ortograficos(descripcion):
    

    x = re.search('[B|V]', descripcion)
    x = re.findall("[{}¿�?]|KK|QW|WR|JL|VB|VT|ÑT|EMBRAGE|UUU|ISQ|AAAA|BBB|CCCC|EEE|HHKG", descripcion)
    if(x):
        print("caracteres raros: ",row[0]," D:",descripcion)
        return 1

    #AAAA|BBB|CCCC
    # if(x):
    #     pass
    #     print("B o V: ",row[0]," D:",descripcion)
    # x = re.search('(TAMOR|V)', descripcion)
    # if(x):
        
    #    # print("TAM*OR: ",row[0]," D:",descripcion)
    #     return 1
    return 0

codigo = []
inventario_industrial = []
inventario_laserena = []
inventario_matriz = []
inventario_bodega = []
descripcion = []
tipo_error = []

fecha_compra_industrial = []
fecha_compra_laserena = []
fecha_compra_matriz = []
fecha_compra_bodega = []

fecha_venta_industrial = []
fecha_venta_laserena = []
fecha_venta_matriz = []
fecha_venta_bodega = []


codigos_industrial = []
codigos_laserena = []
codigos_matriz = []
codigos_bodega = []

inv_industrial = []
inv_laserena = []
inv_matriz = []
inv_bodega = []
contador = 0
guarda_codigos()

maestra =  open ("./database/Maestra.csv","r")
csvreader = csv.reader(maestra, delimiter=',')


for row in csvreader:

        if(row[1]=='' or row[1].isspace()):
           # print("La descripcion esta vacia")
            codigo.append(row[0])
            descripcion.append('Vacio')
            tipo_error.append("Descripcion vacia")
            inventario_laserena.append(inventariado_laserena(row[0]))
            inventario_industrial.append(inventariado_industrial(row[0]))
            inventario_matriz.append(inventariado_matriz(row[0]))
            inventario_bodega.append(inventariado_bodega(row[0]))
        else:
            descripcion_sin_espacios = str(row[1]).replace(" ","")
            #print(descripcion_acortada)
            #time.sleep(1)
            contador = contador + errores_ortograficos(row[1].rstrip())
            #
            # x = re.search('^([OMBILLA]+)|OMBILLA$', txt)
            
    
            if(descripcion_sin_espacios.isdigit()):
            #    print("La descripcion es un numero", descripcion_sin_espacios, "Codigo: ",row[0])
                codigo.append(row[0])
                descripcion.append(row[1])
                tipo_error.append("Solo numeros")
                inventario_laserena.append(inventariado_laserena(row[0]))
                inventario_industrial.append(inventariado_industrial(row[0]))
                inventario_matriz.append(inventariado_matriz(row[0]))
                inventario_bodega.append(inventariado_bodega(row[0]))
            else:
                descripcion_separada = str(row[1]).split()
                #  print(descripcion_separada)
                # print( len(descripcion_separada))
                if(descripcion_separada[0].isalpha() and len(descripcion_separada[0]) == 1 and len(descripcion_separada) == 2 and ((row[9] == '' and row[11] == '') or (row[9] != '' and row[11] == '') or (row[9] == '' and row[11] != ''))):
                    #print("fecha ultima compra:",row[9],"fecha ultima venta:" ,row[11])
                    
                    #print("La descripcion empieza con una letra:", row[1])
                    codigo.append(row[0])
                    descripcion.append((row[1]).rstrip())
                    tipo_error.append("Empieza con letra")
                    inventario_laserena.append(inventariado_laserena(row[0]))
                    inventario_industrial.append(inventariado_industrial(row[0]))
                    inventario_matriz.append(inventariado_matriz(row[0]))
                    inventario_bodega.append(inventariado_bodega(row[0]))
                    fecha_compra_matriz.append(fecha(row[9]))
                    fecha_venta_matriz.append(fecha(row[11]))
                    fecha_compra_industrial.append(fecha(row[9]))
                    fecha_venta_industrial.append(fecha(row[11]))
                    fecha_compra_laserena.append(fecha(row[9]))
                    fecha_venta_laserena.append(fecha(row[11]))
                    fecha_compra_bodega.append(fecha(row[9]))
                    fecha_venta_bodega.append(fecha(row[11]))


print("Total de errores ortograficos: ",contador    )                          
maestra.close()



palabras_vacias = pandas.DataFrame(list(zip(codigo,tipo_error,descripcion,inventario_industrial,fecha_compra_industrial,fecha_venta_industrial,inventario_laserena,fecha_compra_laserena,fecha_venta_laserena,inventario_matriz,fecha_compra_matriz,fecha_venta_matriz,inventario_bodega,fecha_compra_bodega,fecha_venta_bodega)), columns =["Codigo",'Tipo error', 'Descripcion',"I.Industrial","Ult. compra Industrial","Ult. venta Industrial","I.La Serena","Ult. compra La Serena","Ult. venta La Serena","I.Matriz","Ult. compra Matriz","Ult. venta Matriz","I.Bodega","Ult. compra Bodega","Ult. venta Bodega"])
palabras_vacias.to_csv(r'./errores.csv', header={"Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega"}, index=False, sep=',', mode='w')
#palabras_empieza_numero = pandas.DataFrame(list(zip(codigo_palabra_empieza_numero,descripcion_palabra_empieza_numero,inventario_industrial,inventario_laserena)), columns =["Codigo", 'Descripcion',"Inventario Industrial","Inventario La Serena"])
print("Archivo generado \n")
table= tabulate(palabras_vacias, headers = 'keys', tablefmt = 'psql')
#print(table)
#print("Palabras que empiezan con numero: \n",tabulate(palabras_empieza_numero, headers = 'keys', tablefmt = 'github'))
