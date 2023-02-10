import csv,datetime



maestra =  open ("./database/maestra 8-2-23.csv","r")
csvreader = csv.reader(maestra, delimiter=',')
i = 1
for row in csvreader:
    fecha_compra =row[9]
    fecha_venta = row[11]
    
    if((fecha_compra == None or fecha_compra == "" or fecha_compra.isspace() or fecha_venta == None or fecha_venta == "" or fecha_venta.isspace())):
        pass
    else:
        if(fecha_compra[0].isdigit() and fecha_venta[0].isdigit()):
            
            # print(fecha_compra[0],fecha_venta[0])
            dia_compra = int(fecha_compra[0:2])
            mes_compra = int(fecha_compra[2:4])
            anio_compra = int(fecha_compra[4:8])
            
            dia_venta = int(fecha_venta[0:2])
            mes_venta = int(fecha_venta[2:4])
            anio_venta = int(fecha_venta[4:8])

            
            if(dia_compra < 32 and dia_venta <   32 and mes_compra < 13 and mes_venta < 13):
               
                fecha_compra = datetime.datetime(anio_compra, mes_compra, dia_compra)
                fecha_venta  = datetime.datetime(anio_venta, mes_venta, dia_venta)

                if(fecha_compra > fecha_venta):
                    print("N:",i," Codigo",row[0],"Descripcion",row[1],"Fecha Compra",fecha_compra,"Fecha Venta",fecha_venta)
                    i = i +1
                    
    
maestra.close()