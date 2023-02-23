import csv,funciones,pandas,time
from tqdm import tqdm

#Programa que comprueba que los codigos de las sucursales esten en la maestra

if(isinstance(funciones.compruebaBasededatos(), str)):  #Verifica si existen las bases de datos
    print(funciones.compruebaBasededatos()) #Imprime cual base de datos no existe
    input("Presione enter para salir...")
    exit()


NAME_FILE = "Codigos que no estan en la Maestra.csv"

codigos_maestra,codigos_la_serena,codigos_barrio_industrial,codigos_bodega,codigos_matriz = [],[],[],[],[]

maestra =  open (funciones.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        
        codigos_maestra.append(row[0])
maestra.close()

la_serena =  open (funciones.LASERENA_PATH,"r")
csvreader = csv.reader(la_serena, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        codigos_la_serena.append(row[0])   #Guarda los codigos de la sucursal la serena
la_serena.close()

barrio_industrial =  open (funciones.INDUSTRIAL_PATH,"r")
csvreader = csv.reader(barrio_industrial, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        codigos_barrio_industrial.append(row[0])  #Guarda los codigos de la sucursal barrio industrial
barrio_industrial.close()

bodega =  open (funciones.BODEGA_PATH,"r")
csvreader = csv.reader(bodega, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        codigos_bodega.append(row[0])  #Guarda los codigos de la sucursal bodega central
bodega.close()

matriz =  open (funciones.MATRIZ_PATH,"r")
csvreader = csv.reader(matriz, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        codigos_matriz.append(row[0]) #Guarda los codigos de la sucursal casa matriz
matriz.close()

print("Cantidad de codigos en la maestra: ",len(codigos_maestra))
print("Cantidad de codigos en la serena: ",len(codigos_la_serena))
print("Cantidad de codigos en el barrio industrial: ",len(codigos_barrio_industrial))
print("Cantidad de codigos en la bodega central: ",len(codigos_bodega))
print("Cantidad de codigos en la casa matriz: ",len(codigos_matriz))


ubicacion,codigo,inventariado,fecha_compra,fecha_venta = [],[],[],[],[]

print("Sucursal La Serena:")
for i in tqdm(range(len(codigos_la_serena))):
    if(codigos_la_serena[i] not  in codigos_maestra):  #Compara los codigos de la serena con los de la maestra
        ubicacion.append("La Serena")
        codigo.append(codigos_la_serena[i])
        inventariado.append(funciones.getInventarioLaserena(codigos_la_serena[i]))
        fecha_compra.append(funciones.getFechacompraventalaserena(codigos_la_serena[i])[0])
        fecha_venta.append(funciones.getFechacompraventalaserena(codigos_la_serena[i])[1])
        
print("Sucursal Barrio Industrial:")
for i in tqdm(range(len(codigos_barrio_industrial))):
    if(codigos_barrio_industrial[i] not in codigos_maestra):  #Compara los codigos del barrio industrial con los de la maestra
        ubicacion.append("Barrio Industrial")
        codigo.append(codigos_barrio_industrial[i])
        inventariado.append(funciones.getInventarioIndustrial(codigos_barrio_industrial[i]))
        fecha_compra.append(funciones.getFechacompraventaindustrial(codigos_barrio_industrial[i])[0])
        fecha_venta.append(funciones.getFechacompraventaindustrial(codigos_barrio_industrial[i])[1])

print("Sucursal Bodega Central:")
for i in tqdm(range(len(codigos_bodega))):
    if(codigos_bodega[i] not in codigos_maestra):  #Compara los codigos de la bodega central con los de la maestra
        ubicacion.append("Bodega central")
        codigo.append(codigos_bodega[i])
        inventariado.append(funciones.getInventarioBodega(codigos_bodega[i]))
        fecha_compra.append(funciones.getFechacompraventabodega(codigos_bodega[i])[0])
        fecha_venta.append(funciones.getFechacompraventabodega(codigos_bodega[i])[1])

print("Sucursal Casa Matriz:")    
for i in tqdm(range(len(codigos_matriz))):
    if(codigos_matriz[i] not in codigos_maestra):  #Compara los codigos de la casa matriz con los de la maestra
        ubicacion.append("Casa Matriz")
        codigo.append(codigos_matriz[i])
        inventariado.append(funciones.getInventarioMatriz(codigos_matriz[i]))
        fecha_compra.append(funciones.getFechacompraventamatriz(codigos_matriz[i])[0])
        fecha_venta.append(funciones.getFechacompraventamatriz(codigos_matriz[i])[1])

try: #Intenta generar el archivo
    funciones.verificaCarpeta()  #Verifica si existe la carpeta de resultados, si no la crea
    codigos_no_maestra = pandas.DataFrame(list(zip(ubicacion,codigo,inventariado,fecha_compra,fecha_venta)), columns =["Sucursal","Codigo","Inventariado","Fecha de compra sucursal","Fecha de venta sucursal"])
    codigos_no_maestra.to_csv(r''+funciones.RESULTS_PATH+NAME_FILE, header={"Sucursal","Codigo","Inventariado","Fecha de compra sucursal","Fecha de venta sucursal"}, index=False, sep=',', mode='w')
    print("Archivo "+NAME_FILE+" generado correctamente")
    input("Presione enter para salir...")
except:
    print("Error al generar el archivo "+NAME_FILE)
    input("Presione enter para salir...")
    exit()
