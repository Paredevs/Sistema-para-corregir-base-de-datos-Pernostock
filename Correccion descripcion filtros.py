import funciones,csv,time,pandas,re,math
from tqdm import tqdm
from collections import Counter


def buscasinfiltro(descripcion):
    
    x = re.findall("FILTRO", descripcion)
    if(x):
        return True
    return False

codigo,descripcion,inventario_matriz,inventario_bodega,inventario_laserena,inventario_industrial,fecha_compra,fecha_venta = [],[],[],[],[],[],[],[]


inv_matriz = dict(funciones.guarda_inventario_matriz())
inv_bodega = dict(funciones.guarda_inventario_bodega())
inv_serena = dict(funciones.guarda_inventario_laserena())
inv_industrial = dict(funciones.guarda_inventario_industrial())


maestra =  open (funciones.MAESTRA_PATH,"r")
csvreader = csv.reader(maestra, delimiter=',')
i = 0
filtros ={}
confiltro,sinfiltro = [],[]
# for row in tqdm(csvreader):
for row in csvreader:
    if(row[4].strip() == "FILTROS" ):
        descripcion=row[1].rstrip()
        # time.sleep(0.8)
        if(buscasinfiltro(descripcion)): 
            confiltro.append(descripcion)    
        else:
            sinfiltro.append(descripcion)    
    
        # filtros[row[0]]=row[1]
        # codigo.append(row[0])
        # descripcion.append(row[1])
        # inventario_matriz.append(inv_matriz.get(row[0]))
        # inventario_bodega.append(inv_bodega.get(row[0]))
        # inventario_laserena.append(inv_serena.get(row[0]))
        # inventario_industrial.append(inv_industrial.get(row[0]))
        # fecha_compra.append(funciones.getFechacompraventaMaestra(row[0])[0])
        # fecha_venta.append(funciones.getFechacompraventaMaestra(row[0])[1])
        i = i + 1

maestra.close()

print("Cantidad de productos con filtro: ",len(confiltro))
print("Cantidad de productos sin filtro: ",len(sinfiltro))
input("Presione enter para continuar")
# for key in filtros:
#     print(key,"-->",filtros[key])


# for i in confiltro:
#     print(i)
#     time.sleep(0.8)

# print(sinfiltro)
for i in sinfiltro:
    x= re.findall(".*[0-9].*", i)
    if(x):
        print(i)
        input("Presione enter para continuar")


counterA = Counter(confiltro)
counterB = Counter(sinfiltro)

terms = set(counterA).union(counterB)
dotprod = sum(counterA.get(k, 0) * counterB.get(k, 0) for k in terms)
magA = math.sqrt(sum(counterA.get(k, 0)**2 for k in terms))
magB = math.sqrt(sum(counterA.get(k, 0)**2 for k in terms))
print(dotprod / (magA * magB))



filtros= pandas.DataFrame(list(zip(codigo,descripcion,fecha_compra,fecha_venta,inventario_bodega,inventario_matriz,inventario_laserena,inventario_industrial)), columns =["Codigo","Descripcion","Fecha Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"])
filtros.to_csv(r'./resultados/Correccion de filtros.csv', header={"Codigo","Descripcion","Fechac Compra","Fecha Venta","Inv Bodega","Inv Matriz","Inv Serena","Inv Industrial"}, index=True, sep=',', mode='w')
print("Archivo generado correctamente - Cantidad de productos: ",i)