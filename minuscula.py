import csv
maestra =  open ("./database/maestra 8-2-23.csv","r")
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    if( row[1].islower()):
        print("Codigo",row[0],"Descripcion",row[1])
maestra.close()