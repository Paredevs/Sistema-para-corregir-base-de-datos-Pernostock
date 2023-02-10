import csv,time
tiempo=3
maestra =  open ("./database/maestra 8-2-23.csv","r")
la_serena =  open ("./database/la serena.csv","r")
barrio_industrial =  open ("./database/barrio_industrial.csv","r")
bodega =  open ("./database/bodega.csv","r")
matriz =  open ("./database/matriz.csv","r")


condigos_maestra = []
condigos_la_serena = []
condigos_barrio_industrial = []
condigos_bodega = []
condigos_matriz = []

contador = 0
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    contador = contador + 1
    #print(contador," Codigos maestra",row[0])
    condigos_maestra.append(row[0])

time.sleep(tiempo)
contador = 0
csvreader = csv.reader(la_serena, delimiter=',')
for row in csvreader:
    contador = contador + 1
    #print(contador," Codigos la serena",row[0])
    condigos_la_serena.append(row[0])

time.sleep(tiempo)

contador = 0
csvreader = csv.reader(barrio_industrial, delimiter=',')
for row in csvreader:
    contador = contador + 1
    #print(contador,"Codigos barrio industrial",row[0])
    condigos_barrio_industrial.append(row[0])

time.sleep(tiempo)

csvreader = csv.reader(bodega, delimiter=',')

contador = 0
for row in csvreader:
    contador = contador + 1
    #print(contador," Codigos bodega",row[0])
    condigos_bodega.append(row[0])

time.sleep(tiempo)

contador = 0
csvreader = csv.reader(matriz, delimiter=',')
for row in csvreader:
    contador = contador + 1
    #
    # print(contador," Codigos matriz",row[0])
    condigos_matriz.append(row[0])

maestra.close()
la_serena.close()
barrio_industrial.close()
bodega.close()
matriz.close()


for i in range(len(condigos_la_serena)):
    if(condigos_la_serena[i] in condigos_maestra):
        #print("El codigo",condigos_la_serena[i],"esta en la maestra")
        pass
    else:
        print("El codigo de la serena:",condigos_la_serena[i],"no esta en la maestra")
        time.sleep(tiempo)

for i in range(len(condigos_barrio_industrial)):
    if(condigos_barrio_industrial[i] in condigos_maestra):
        #print("El codigo",condigos_barrio_industrial[i],"esta en la maestra")
        pass
    else:
        print("El codigo de barrio industrial:",condigos_barrio_industrial[i],"no esta en la maestra")
        time.sleep(tiempo)

for i in range(len(condigos_bodega)):
    if(condigos_bodega[i] in condigos_maestra):
        #print("El codigo",condigos_bodega[i],"esta en la maestra")
        pass
    else:
        print("El codigo de bodega: ",condigos_bodega[i],"no esta en la maestra")
        time.sleep(tiempo)

for i in range(len(condigos_matriz)):
    if(condigos_matriz[i] in condigos_maestra):
        #print("El codigo",condigos_matriz[i],"esta en la maestra")
        pass
    else:
        print("El codigo de casa matriz: ",condigos_matriz[i],"no esta en la maestra")
        time.sleep(tiempo)


   


