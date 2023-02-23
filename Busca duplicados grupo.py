
#Programa para detectar productos duplicados dependiendo de la familia
#Pendiente
import csv,time,funciones
entries = []
duplicate_entries = []
rotacion =  open (funciones.RESULTS_PATH,"r") #Se necesita un csv solo con los productos de rotacion
csvreader = csv.reader(rotacion, delimiter=',')
for row in csvreader:
    if row[2] not in entries:
        entries.append(row[2])
    else:
        duplicate_entries.append(row[2]) 
rotacion.close()
print("Cantidad de productos con rotacion duplicados: ",len(duplicate_entries))
