import sucursal,csv,time,pandas
from tqdm import tqdm

codigo,descripcion,inventario_matriz,inventario_bodega,inventario_laserena,inventario_industrial,fecha_compra,fecha_venta = [],[],[],[],[],[],[],[]

if(sucursal.compruebaBasededatos() == False):  #Verifica si existen las bases de datos
    print("Falta el archivo maestra.csv o alguna base de datos de las sucursales")
    input("Presione enter para salir...")
    exit()
    
inv_matriz = dict(sucursal.guarda_inventario_matriz())
inv_bodega = dict(sucursal.guarda_inventario_bodega())
inv_serena = dict(sucursal.guarda_inventario_laserena())
inv_industrial = dict(sucursal.guarda_inventario_industrial())

grupo=str(input("Ingrese el grupo de productos a buscar:"))
grupo = grupo.upper()
maestra =  open (sucursal.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
i = 0
for row in tqdm(csvreader):
    
    if(row[4].strip() == grupo.strip()):
        
        codigo.append(row[0])
        descripcion.append(row[1])
        inventario_matriz.append(inv_matriz.get(row[0]))
        inventario_bodega.append(inv_bodega.get(row[0]))
        inventario_laserena.append(inv_serena.get(row[0]))
        inventario_industrial.append(inv_industrial.get(row[0]))
        fecha_compra.append(sucursal.setFecha(row[9]))
        fecha_venta.append(sucursal.setFecha(row[11]))
        i = i + 1   
       
maestra.close()




rotacion= pandas.DataFrame(list(zip(codigo,descripcion,fecha_compra,fecha_venta,inventario_bodega,inventario_matriz,inventario_laserena,inventario_industrial)), columns =["Codigo","Descripcion","Fecha Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"])
rotacion.to_csv(r'./results/Movimiento de grupo/movimiento_'+grupo+'.csv', header={"Codigo","Descripcion","Fechac Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"}, index=True, sep=',', mode='w')
print("Archivo generado correctamente - Cantidad de productos: ",i)

# entries = []
# duplicate_entries = {}
# rotacion =  open ("./results/movimiento_"+grupo+".csv","r")
# csvreader = csv.reader(rotacion, delimiter=',')
# for row in csvreader:
#     if row[2] not in entries:
#         entries.append(row[2])
#     else:
#         duplicate_entries[row[1]] = row[2] 
# rotacion.close()
# # for key in duplicate_entries:
# #     print(key, '->', duplicate_entries[key])
# #     time.sleep(0.5)
# print("Cantidad de productos con ",grupo," duplicados: ",len(duplicate_entries))

