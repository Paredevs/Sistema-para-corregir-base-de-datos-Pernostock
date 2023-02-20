import funciones,pandas


#Programa creado para buscar duplicados exactos en todas las bases de datos (Maestra, Bodega, Matriz, La Serena, Industrial) y agruparlos por codigo de producto

if(funciones.compruebaBasededatos() == False):  #Verifica si existen las bases de datos
    print("Falta el archivo maestra.csv o alguna base de datos de las sucursales")
    input("Presione enter para salir...")
    exit()


duplicados_unicos,familia,lista_duplicados = [],[],[]
base_datos= int(input("Ingrese el nombre de la base de datos a buscar: \n1) Maestra 2) Bodega central 3) Casa matriz 4) La Serena 5) Industrial: "))
if(base_datos == 1): #Busca los duplicados en la maestra
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.MAESTRA_PATH,1))
    FILE_NAME = "MAESTRA Duplicados exactos agrupados.csv"
elif(base_datos == 2):  #Busca los duplicados en la bodega central
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.BODEGA_PATH,2))
    FILE_NAME = "BODEGA CENTRAL Duplicados exactos agrupados.csv"
elif(base_datos == 3):  #Busca los duplicados en la casa matriz
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.MATRIZ_PATH,2))
    FILE_NAME = "CASA MATRIZ Duplicados exactos agrupados.csv"
elif(base_datos == 4):   #Busca los duplicados en la sucursal la serena
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.LASERENA_PATH,2))
    FILE_NAME = "LA SERENA Duplicados exactos agrupados.csv"
elif(base_datos == 5):   #Busca los duplicados en la sucursal  barrio industrial
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.INDUSTRIAL_PATH,2))
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
    familia.append(funciones.getFamilia(key))
    lista_duplicados.append(lista)


try:
    funciones.verificaCarpeta()  #Veriiica si existe la carpeta de resultados
    palabras_vacias = pandas.DataFrame(list(zip(duplicados_unicos,familia,lista_duplicados)), columns =["Descripcion","Familia","Codigos donde esta duplicado"])
    palabras_vacias.to_csv(r''+funciones.RESULTS_PATH+FILE_NAME, header={"Descripcion","Familia","Codigos donde esta duplicado"}, index=True, sep=',', mode='w')
except Exception as e: 
    print("Error al generar el archivo ",FILE_NAME)
    print(e)
    input("Presione enter para continuar...")
    exit()
print("Archivo generado correctamente en "+funciones.RESULTS_PATH)
input("Presione enter para salir")
exit()