import csv,sucursal,pandas
from tqdm import tqdm

#Programa que comprueba que los codigos de las sucursales esten en la maestra

if(sucursal.compruebaBasededatos() == False):  #Verifica si existen las bases de datos
    print("Falta el archivo maestra.csv o alguna base de datos de las sucursales")
    input("Presione enter para salir...")
    exit()


NAME_FILE = "Codigos que no estan en Maestra.csv"

condigos_maestra,condigos_la_serena,condigos_barrio_industrial,condigos_bodega,condigos_matriz = [],[],[],[],[]

maestra =  open (sucursal.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    condigos_maestra.append(row[0])
maestra.close()

la_serena =  open (sucursal.LASERENA_PATH,"r")
csvreader = csv.reader(la_serena, delimiter=',')
for row in csvreader:
    if(sucursal.esCodigo(row)):
        condigos_la_serena.append(row[0])   #Guarda los codigos de la sucursal la serena
la_serena.close()

barrio_industrial =  open (sucursal.INDUSTRIAL_PATH,"r")
csvreader = csv.reader(barrio_industrial, delimiter=',')
for row in csvreader:
    if(sucursal.esCodigo(row)):
        condigos_barrio_industrial.append(row[0])  #Guarda los codigos de la sucursal barrio industrial
barrio_industrial.close()

bodega =  open (sucursal.BODEGA_PATH,"r")
csvreader = csv.reader(bodega, delimiter=',')
for row in csvreader:
    if(sucursal.esCodigo(row)):
        condigos_bodega.append(row[0])  #Guarda los codigos de la sucursal bodega central
bodega.close()

matriz =  open (sucursal.MATRIZ_PATH,"r")
csvreader = csv.reader(matriz, delimiter=',')
for row in csvreader:
    if(sucursal.esCodigo(row)):
        condigos_matriz.append(row[0]) #Guarda los codigos de la sucursal casa matriz
matriz.close()

ubicacion,codigo,inventariado,fecha_compra,fecha_venta = [],[],[],[],[]

for i in tqdm(range(len(condigos_la_serena))):
    if(condigos_la_serena[i] not  in condigos_maestra):  #Compara los codigos de la serena con los de la maestra
        ubicacion.append("La Serena")
        codigo.append(condigos_la_serena[i])
        inventariado.append(sucursal.getInventarioLaserena(condigos_la_serena[i]))
        fecha_compra.append(sucursal.getFechacompraventalaserena(condigos_la_serena[i])[0])
        fecha_venta.append(sucursal.getFechacompraventalaserena(condigos_la_serena[i])[1])
        

for i in tqdm(range(len(condigos_barrio_industrial))):
    if(condigos_barrio_industrial[i] not in condigos_maestra):  #Compara los codigos del barrio industrial con los de la maestra
        ubicacion.append("Barrio Industrial")
        codigo.append(condigos_barrio_industrial[i])
        inventariado.append(sucursal.getInventarioIndustrial(condigos_barrio_industrial[i]))
        fecha_compra.append(sucursal.getFechacompraventaindustrial(condigos_barrio_industrial[i])[0])
        fecha_venta.append(sucursal.getFechacompraventaindustrial(condigos_barrio_industrial[i])[1])


for i in tqdm(range(len(condigos_bodega))):
    if(condigos_bodega[i] not in condigos_maestra):  #Compara los codigos de la bodega central con los de la maestra
        ubicacion.append("Bodega central")
        codigo.append(condigos_bodega[i])
        inventariado.append(sucursal.getInventarioBodega(condigos_bodega[i]))
        fecha_compra.append(sucursal.getFechacompraventabodega(condigos_bodega[i])[0])
        fecha_venta.append(sucursal.getFechacompraventabodega(condigos_bodega[i])[1])
        
for i in tqdm(range(len(condigos_matriz))):
    if(condigos_matriz[i] not in condigos_maestra):  #Compara los codigos de la casa matriz con los de la maestra
        ubicacion.append("Casa Matriz")
        codigo.append(condigos_matriz[i])
        inventariado.append(sucursal.getInventarioMatriz(condigos_matriz[i]))
        fecha_compra.append(sucursal.getFechacompraventamatriz(condigos_matriz[i])[0])
        fecha_venta.append(sucursal.getFechacompraventamatriz(condigos_matriz[i])[1])


try: #Intenta generar el archivo
    sucursal.verificaCarpeta()  #Verifica si existe la carpeta de resultados, si no la crea
    codigos_no_maestra = pandas.DataFrame(list(zip(ubicacion,codigo,inventariado,fecha_compra,fecha_venta)), columns =["Sucursal","Codigo","Inventariado","Fecha de compra sucursal","Fecha de venta sucursal"])
    codigos_no_maestra.to_csv(r''+sucursal.RESULTS_PATH+NAME_FILE, header={"Sucursal","Codigo","Inventariado","Fecha de compra sucursal","Fecha de venta sucursal"}, index=False, sep=',', mode='w')
    print("Archivo "+NAME_FILE+" generado correctamente")
    input("Presione enter para salir")
except:
    print("Error al generar el archivo "+NAME_FILE)
    input("Presione enter para salir...")
    exit()


