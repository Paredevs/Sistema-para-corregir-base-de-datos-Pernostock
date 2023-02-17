import csv,sucursal,pandas
import numpy as np

#Programa creado para buscar duplicados exactos en todas las bases de datos (Maestra, Bodega, Matriz, La Serena, Industrial) y agruparlos por codigo de producto

duplicados_unicos = []
lista_duplicados = []
base_datos= int(input("Ingrese el nombre de la base de datos a buscar: \n1) Maestra 2) Bodega 3) Matriz 4) La Serena 5) Industrial: "))
if(base_datos == 1):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.MAESTRA_PATH,1))
    nombre_archivo = "Maestra"
elif(base_datos == 2):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.BODEGA_PATH,2))
    nombre_archivo = "Bodega central"
elif(base_datos == 3):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.MATRIZ_PATH,2))
    nombre_archivo = "Casa matriz"
elif(base_datos == 4):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.LASERENA_PATH,2))
    nombre_archivo = "La Serena"
elif(base_datos == 5):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.INDUSTRIAL_PATH,2))
    nombre_archivo = "Barrio industrial"
else:
    print("Opcion invalida")
    exit()
print("Cantidad de productos unicos duplicados: ",len(dic_duplicados))
total_duplicados = sum(len(l) for l in list(dic_duplicados.values()))
print("Cantidad de descripciones duplicadas: ",total_duplicados)

for key, value in dic_duplicados.items():
    duplicados_unicos.append(key)
    lista = " - ".join(value)

    lista_duplicados.append(lista)

palabras_vacias = pandas.DataFrame(list(zip(duplicados_unicos,lista_duplicados)), columns =["Descripcion","Codigos donde esta duplicado"])
palabras_vacias.to_csv(r'./results/Duplicados exactos agrupados/'+nombre_archivo+' Duplicados exactos agrupados.csv', header={"Descripcion","Codigos donde esta duplicado"}, index=True, sep=',', mode='w')
