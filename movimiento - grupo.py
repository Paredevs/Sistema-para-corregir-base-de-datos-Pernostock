import funciones,csv,time,pandas
from tqdm import tqdm

codigo,descripcion,inventario_matriz,inventario_bodega,inventario_laserena,inventario_industrial,fecha_compra,fecha_venta = [],[],[],[],[],[],[],[]

if(isinstance(funciones.compruebaBasededatos(), str)):  #Verifica si existen las bases de datos
    print(funciones.compruebaBasededatos()) #Imprime cual base de datos no existe
    input("Presione enter para salir...")
    exit()
    
inv_matriz = dict(funciones.guarda_inventario_matriz())
inv_bodega = dict(funciones.guarda_inventario_bodega())
inv_serena = dict(funciones.guarda_inventario_laserena())
inv_industrial = dict(funciones.guarda_inventario_industrial())

grupo=str(input("Ingrese el grupo de productos a buscar:"))
grupo = grupo.upper()
file_name = "movimiento - "+grupo + ".csv"
maestra =  open (funciones.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
i = 0
for row in tqdm(csvreader):
    if(funciones.esCodigo(row)):
        if(row[4].strip() == grupo.strip()):

            codigo.append(row[0])
            descripcion.append(row[1])
            inventario_matriz.append(inv_matriz.get(row[0]))
            inventario_bodega.append(inv_bodega.get(row[0]))
            inventario_laserena.append(inv_serena.get(row[0]))
            inventario_industrial.append(inv_industrial.get(row[0]))
            fecha_compra.append(funciones.setFecha(row[9]))
            fecha_venta.append(funciones.setFecha(row[11]))
            i = i + 1   
       
maestra.close()

try:
    funciones.verificaCarpeta()  #Veriiica si existe la carpeta de resultados
    movimiento= pandas.DataFrame(list(zip(codigo,descripcion,fecha_compra,fecha_venta,inventario_bodega,inventario_matriz,inventario_laserena,inventario_industrial)), columns =["Codigo","Descripcion","Fecha Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"])
    movimiento.to_csv(r''+funciones.RESULTS_PATH+file_name, header={"Codigo","Descripcion","Fechac Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"}, index=False, sep=',', mode='w')
except:
    print("Error al generar el archivo ",file_name)
    input("Presione enter para continuar...")
    exit()
print("Archivo ",file_name," generado correctamente en "+funciones.RESULTS_PATH+"\nCantidad de productos: ",i)
input("Presione enter para salir")
exit()