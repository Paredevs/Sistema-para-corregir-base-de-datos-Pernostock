import csv,funciones


maestra =  open (funciones.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    descripcion = row[1].strip()
    if(descripcion.isdigit()):
        print(descripcion)
        input("Presione enter para continuar")
    
    
maestra.close()

bodega =  open (funciones.BODEGA_PATH,"r")
csvreader = csv.reader(bodega, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        descripcion = row[1].strip()
        if(descripcion.isdigit()):
            print("Bodega",descripcion)
            input("Presione enter para continuar")

bodega.close()

matriz =  open (funciones.MATRIZ_PATH,"r")
csvreader = csv.reader(matriz, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        descripcion = row[1].strip()
        if(descripcion.isdigit()):
            print("Matriz",descripcion)
            input("Presione enter para continuar")

matriz.close()

laserena =  open (funciones.LASERENA_PATH,"r")
csvreader = csv.reader(laserena, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        descripcion = row[1].strip()
        if(descripcion.isdigit()):
            print("la serena",descripcion)
            input("Presione enter para continuar")

laserena.close()

industrial =  open (funciones.INDUSTRIAL_PATH,"r")
csvreader = csv.reader(industrial, delimiter=',')
for row in csvreader:
    if(funciones.esCodigo(row)):
        descripcion = row[1].strip()
        if(descripcion.isdigit()):
            print("industrial",descripcion)
            input("Presione enter para continuar")

industrial.close()
