import csv,time

errors = []

contador=1
indice=1
file =  open ("./sugerencia_compras__2023 Arreglado python.csv","r")
csvreader = csv.reader(file, delimiter=',')
for row in csvreader:
    #print("Codigo",row[0],"Cod.Proveedor","Descripcion Producto","familia","linea","Inventario","Rotacion","Dia ventas","Ventas","Stock Actual","stock Minimo,Stock Seguridad,Stock Maximo,Ventas Proyectadas,Pendientes en O/C.,Sugerida a Comprar,Precio Lista Proveedor,Total Compra,Proveedor,Proveedor Ultima compra,Fecha Ultima compra,Valor ultima compra,Fecha Ulima Venta,Valor ult.Venta)
    print("Codigo",row[0])
    time.sleep(1)