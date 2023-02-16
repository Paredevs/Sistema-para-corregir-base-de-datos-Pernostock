import csv,sucursal

#Programa creado para buscar duplicados exactos en todas las bases de datos (Maestra, Bodega, Matriz, La Serena, Industrial)


base_datos= int(input("Ingrese el nombre de la base de datos a buscar: \n1) Maestra 2) Bodega 3) Matriz 4) La Serena 5) Industrial: "))
if(base_datos == 1):
    sucursal.duplicadosExactos(sucursal.MAESTRA_PATH)
elif(base_datos == 2):
    sucursal.duplicadosExactos(sucursal.BODEGA_PATH)
elif(base_datos == 3):
    sucursal.duplicadosExactos(sucursal.MATRIZ_PATH)
elif(base_datos == 4):
    sucursal.duplicadosExactos(sucursal.LASERENA_PATH)
elif(base_datos == 5):
    sucursal.duplicadosExactos(sucursal.INDUSTRIAL_PATH)