import sucursal,pandas


#Programa creado para buscar duplicados exactos en todas las bases de datos (Maestra, Bodega, Matriz, La Serena, Industrial) y agruparlos por codigo de producto

if(sucursal.compruebaBasededatos() == False):  #Verifica si existen las bases de datos
    print("Falta el archivo maestra.csv o alguna base de datos de las sucursales")
    input("Presione enter para salir...")
    exit()


duplicados_unicos,lista_duplicados = [],[]
base_datos= int(input("Ingrese el nombre de la base de datos a buscar: \n1) Maestra 2) Bodega 3) Matriz 4) La Serena 5) Industrial: "))
if(base_datos == 1):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.MAESTRA_PATH,1))
    FILE_NAME = "MAESTRA Duplicados exactos agrupados.csv"
elif(base_datos == 2):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.BODEGA_PATH,2))
    FILE_NAME = "BODEGA CENTRAL Duplicados exactos agrupados.csv"
elif(base_datos == 3):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.MATRIZ_PATH,2))
    FILE_NAME = "CASA MATRIZ Duplicados exactos agrupados.csv"
elif(base_datos == 4):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.LASERENA_PATH,2))
    FILE_NAME = "LA SERENA Duplicados exactos agrupados.csv"
elif(base_datos == 5):
    dic_duplicados = dict(sucursal.duplicadosExactosAgrupados(sucursal.INDUSTRIAL_PATH,2))
    FILE_NAME = "INDUSTRIAL Duplicados exactos agrupados.csv"
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

try:
    sucursal.verificaCarpeta()  #Veriiica si existe la carpeta de resultados
    palabras_vacias = pandas.DataFrame(list(zip(duplicados_unicos,lista_duplicados)), columns =["Descripcion","Codigos donde esta duplicado"])
    palabras_vacias.to_csv(r''+sucursal.RESULTS_PATH+'Duplicados exactos agrupados/'+FILE_NAME, header={"Descripcion","Codigos donde esta duplicado"}, index=True, sep=',', mode='w')
except:
    print("Error al generar el archivo ",FILE_NAME)
    input("Presione enter para continuar...")