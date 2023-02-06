import csv,time,pandas,numpy as np
from tabulate import tabulate


from tqdm import tqdm


     



def agrega_inventarios(codigo):

    inventario_laserena.append(inventariado_laserena(codigo))
    inventario_industrial.append(inventariado_industrial(codigo))
    inventario_matriz.append(inventariado_matriz(codigo))
    inventario_bodega.append(inventariado_bodega(codigo))
    
def inventariado_industrial(codigo):

    inicio = 0
    industrial = open ("./database/barrio_industrial.csv","r")
    csvreader = csv.reader(industrial, delimiter=',')
    for row in csvreader:
       # if(inicio==3):
            if(row[0]==codigo):
                return row[5]

        #else:
         #  inicio = inicio + 1

    industrial.close()
    return ""

def inventariado_laserena(codigo):

    inicio = 0
    laserena = open ("./database/la serena.csv","r")
    csvreader = csv.reader(laserena, delimiter=',')
    for row in csvreader:
       # if(inicio==3):
            if(row[0]==codigo):

                return row[5]
        #else:
         #  inicio = inicio + 1

    laserena.close()
    return ""

def inventariado_matriz(codigo):

    inicio = 0
    matriz = open ("./database/matriz.csv","r")
    csvreader = csv.reader(matriz, delimiter=',')
    for row in csvreader:
       # if(inicio==3):
            if(row[0]==codigo):

                return row[5]
        #else:
         #  inicio = inicio + 1

    matriz.close()
    return ""  

def inventariado_bodega(codigo):

    inicio = 0
    bodega = open ("./database/bodega.csv","r")
    csvreader = csv.reader(bodega, delimiter=',')
    for row in csvreader:
       # if(inicio==3):
            if(row[0]==codigo):

                return row[5]
        #else:
         #  inicio = inicio + 1

    bodega.close()
    return ""  




maestra =  open ("./database/Maestra.csv","r")

csvreader = csv.reader(maestra, delimiter=',')



codigo = []
inventario_industrial = []
inventario_laserena = []
inventario_matriz = []
inventario_bodega = []
descripcion = []

stock_industrial = []
stock_laserena = []
stock_matriz = []
stock_bodega = []

tipo_error = []


for row in csvreader:

        # print(row[1])
        
        #print(letra_descripcion)
        if(row[1]=='' or row[1].isspace()):
            print("La descripcion esta vacia")
            codigo.append(row[0])
            descripcion.append('Vacio')
            tipo_error.append("Descripcion vacia")
            agrega_inventarios(row[0])
        else:
    
            descripcion_sin_espacios = str(row[1]).replace(" ","")
            #print(descripcion_acortada)
            #time.sleep(1)
            if(descripcion_sin_espacios.isdigit()):
                
                print("La descripcion es un numero", descripcion_sin_espacios, "Codigo: ",row[0])
                codigo.append(row[0])
                descripcion.append(row[1])
                tipo_error.append("Solo numeros")
                agrega_inventarios(row[0])

            else:
                descripcion_separada = str(row[1]).split()
                #  print(descripcion_separada)
                # print( len(descripcion_separada))
                # if(descripcion_separada[0].isalpha() and len(descripcion_separada[0]) == 1 and len(descripcion_separada) == 2):
                #     print("La descripcion empieza con una letra:", row[1])
                #     codigo.append(row[0])
                #     descripcion.append(row[1])
                #     tipo_error.append("Empieza con letra")
                #     agrega_inventarios(row[0])
                    


            

maestra.close()

palabras_vacias = pandas.DataFrame(list(zip(codigo,tipo_error,descripcion,inventario_industrial,inventario_laserena,inventario_matriz,inventario_bodega)), columns =["Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega"])
palabras_vacias.to_csv(r'C:\Users\Rodrigo', header=None, index=None, sep=' ', mode='a')
#palabras_empieza_numero = pandas.DataFrame(list(zip(codigo_palabra_empieza_numero,descripcion_palabra_empieza_numero,inventario_industrial,inventario_laserena)), columns =["Codigo", 'Descripcion',"Inventario Industrial","Inventario La Serena"])
print("PRODUCTOS ERRONEOS: \n")
print(tabulate(palabras_vacias, headers = 'keys', tablefmt = 'psql'))
#print("Palabras que empiezan con numero: \n",tabulate(palabras_empieza_numero, headers = 'keys', tablefmt = 'github'))
