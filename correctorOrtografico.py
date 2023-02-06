import csv,time,pandas,numpy as np
from tabulate import tabulate


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




  





maestra =  open ("./database/Maestra.csv","r")

csvreader = csv.reader(maestra, delimiter=',')



codigo = []
inventario_industrial = []
inventario_laserena = []
inventario_matriz = []
inventario_bodega = []
descripcion = []
tipo_error = []


codigos_industrial = []
codigos_laserena = []
codigos_matriz = []
codigos_bodega = []

inv_industrial = []
inv_laserena = []
inv_matriz = []
inv_bodega = []






guarda_codigos()

for row in csvreader:

        # print(row[9])
        # print(row[8])
        # print(row[1])
        
        #print(letra_descripcion)
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
                    #print("La descripcion empieza con una letra:", row[1])
                    codigo.append(row[0])
                    descripcion.append((row[1]).rstrip())
                    tipo_error.append("Empieza con letra")
                    inventario_laserena.append(inventariado_laserena(row[0]))
                    inventario_industrial.append(inventariado_industrial(row[0]))
                    inventario_matriz.append(inventariado_matriz(row[0]))
                    inventario_bodega.append(inventariado_bodega(row[0]))
                                
maestra.close()



palabras_vacias = pandas.DataFrame(list(zip(codigo,tipo_error,descripcion,inventario_industrial,inventario_laserena,inventario_matriz,inventario_bodega)), columns =["Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega"])
palabras_vacias.to_csv(r'./errores.csv', header={"Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega"}, index=False, sep=',', mode='w')
#palabras_empieza_numero = pandas.DataFrame(list(zip(codigo_palabra_empieza_numero,descripcion_palabra_empieza_numero,inventario_industrial,inventario_laserena)), columns =["Codigo", 'Descripcion',"Inventario Industrial","Inventario La Serena"])
print("PRODUCTOS ERRONEOS: \n")
table= tabulate(palabras_vacias, headers = 'keys', tablefmt = 'psql')
print(table)
#print("Palabras que empiezan con numero: \n",tabulate(palabras_empieza_numero, headers = 'keys', tablefmt = 'github'))
