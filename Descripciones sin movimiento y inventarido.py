import csv,sucursal,pandas

FILE_NAME = 'Productos sin movimiento y inventariado.csv'
codigo,descripcion,inventario_matriz,grupo,inventario_bodega,inventario_laserena,inventario_industrial,fecha_compra,fecha_venta = [],[],[],[],[],[],[],[],[]

inv_matriz = dict(sucursal.guarda_inventario_matriz())
inv_bodega = dict(sucursal.guarda_inventario_bodega())
inv_serena = dict(sucursal.guarda_inventario_laserena())
inv_industrial = dict(sucursal.guarda_inventario_industrial())

maestra =  open (sucursal.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
i = 0
for row in csvreader:
    
    fecha_compra_actual =row[9]
    fecha_venta_actual = row[11]
    
    
    if((fecha_compra_actual == None or fecha_compra_actual == "" or fecha_compra_actual.isspace()) and (fecha_venta_actual == None or fecha_venta_actual == "" or fecha_venta_actual.isspace())):
        if((inv_matriz.get(row[0]) == None or inv_matriz.get(row[0])=='N') and (inv_bodega.get(row[0]) == None or inv_bodega.get(row[0]) == 'N' ) and (inv_serena.get(row[0]) == None or inv_serena.get(row[0]) == 'N' ) and (inv_industrial.get(row[0]) == None or inv_industrial.get(row[0]) == 'N')):
            codigo.append(row[0])
            descripcion.append(row[1])
            grupo.append(row[4])
            inventario_matriz.append(inv_matriz.get(row[0]))
            inventario_bodega.append(inv_bodega.get(row[0]))
            inventario_laserena.append(inv_serena.get(row[0]))
            inventario_industrial.append(inv_industrial.get(row[0]))
            fecha_compra.append(sucursal.setFecha(row[9]))
            fecha_venta.append(sucursal.setFecha(row[11]))
            i = i + 1
          
       
maestra.close()

try:
    sucursal.verificaCarpeta()
    sin_movimiento= pandas.DataFrame(list(zip(codigo,descripcion,grupo,fecha_compra,fecha_venta,inventario_bodega,inventario_matriz,inventario_laserena,inventario_industrial)), columns =["Codigo","Descripcion","Grupo","Fecha Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"])
    sin_movimiento.to_csv(r''+sucursal.RESULTS_PATH+FILE_NAME, header={"Codigo","Descripcion","Grupo","Fecha Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"}, index=True, sep=',', mode='w')
    print("Archivo ",FILE_NAME," generado correctamente - Cantidad de productos: ",i)
except:
    print("Error al generar el archivo ",FILE_NAME)
    input("Presione enter para continuar...")