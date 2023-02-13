import csv,re,pandas,sucursal
from tqdm import tqdm


def correas():

    maestra =  open ("./database/maestra 8-2-23.csv","r")
    csvreader = csv.reader(maestra, delimiter=',')

    for row in csvreader:
        original.append(row)
        correa_correcta = re.findall("^CORREA \dPK.*|(^CORREA V.* \dPK \d\d\d\d)",row[1].rstrip())
        if(correa_correcta):
            row[1] = row[1].split() #separa la descripcion
    
            if(row[1][0]!="CORREA"):
                print("UNA CORREA ES INCORRECTA: ",row[0]," D:",row[1])
            #print("CORREAS CORRECTAS: ",row[1])
            if(len(row[1])>2):
              #  print("correa con descripcion distinta: ",row[1])
                correa_distinta= ""
                for i in range(len(row[1])):
                    correa_distinta = correa_distinta + row[1][i]
               # print(correa_distinta)
                row[1][0] = correa_distinta
                row[1].remove(row[1][1])
                #print(row[1])
                tmp = []
                tmp.append(row[1][0])
                row[1] = tmp 
                #print(row[1])

                
                
            # time.sleep(0.5)
            
            row[1].append(row[0]) #agrega el codigo
            #print(row[1])
            
            #time.sleep(0.5)
            
        # print(descripcion)
            correas_correctas.append(row[1])
   # print(correas_correctas)
    maestra.close()


def retornadescripcion(codigo):

    for i in range(len(original)):
        # print(original[i])
        # time.sleep(0.5)
        if(original[i][0]==codigo):
            return original[i][1][0]+" "+original[i][1][1]
            # return original[i][1]
    return ""

nombre_columnas = ["C. malo","D. mala","F.Compra","F.Venta","I.bodega","I.matriz","I.serena","I.industrial","C. bueno","D. buena","F.Compra","F.Venta","I.bodega","I.matriz","I.serena","I.industrial"]
correas_correctas = []
correas_incorrectas = []

original = []
correa_incorrecta_codigo = []
correa_incorrecta_descripcion = []
correa_incorrecta_fecha_compra_maestra = []
correa_incorrecta_fecha_venta_maestra = []
correa_incorrecta_inv_bodega = []
correa_incorrecta_inv_matriz = []
correa_incorrecta_inv_serena = []
correa_incorrecta_inv_industrial = []

correa_correcta_codigo = []
correa_correcta_descripcion = []
correa_correcta_fecha_compra_maestra = []
correa_correcta_fecha_venta_maestra = []
correa_correcta_inv_bodega = []
correa_correcta_inv_matriz = []
correa_correcta_inv_serena = []
correa_correcta_inv_industrial = []


correas()


maestra =  open ("./database/maestra 8-2-23.csv","r")
csvreader = csv.reader(maestra, delimiter=',')
for row in csvreader:
    descripcion_separada = str(row[1]).split()
    if(len(descripcion_separada)==1 and len(descripcion_separada[0])>3 and descripcion_separada[0][0].isdigit() and  descripcion_separada[0][1]=="P"):               
        correa_erronea_separada=descripcion_separada[0].split("-")
        correa_erronea_separada[0]=correa_erronea_separada[0]+correa_erronea_separada[1]
        correa_erronea_separada.remove(correa_erronea_separada[1])
        correa_erronea_separada.append(row[0])
        correas_incorrectas.append(correa_erronea_separada)
                        
                

maestra.close()

for correa_incorrecta in tqdm(correas_incorrectas):
    i=1
    for correa_correcta in correas_correctas:

        if(correa_incorrecta[0]==correa_correcta[1]):
        
            correa_incorrecta_codigo.append(correa_incorrecta[1])
            correa_incorrecta_descripcion.append(correa_incorrecta[0])
            correa_incorrecta_fecha_compra_maestra.append(sucursal.fecha_compra(correa_incorrecta[1]))
            correa_incorrecta_fecha_venta_maestra.append(sucursal.fecha_venta(correa_incorrecta[1]))
            correa_incorrecta_inv_bodega.append(sucursal.inventario_bodega(correa_incorrecta[1]))
            correa_incorrecta_inv_matriz.append(sucursal.inventario_matriz(correa_incorrecta[1]))
            correa_incorrecta_inv_serena.append(sucursal.inventario_laserena(correa_incorrecta[1]))
            correa_incorrecta_inv_industrial.append(sucursal.inventario_industrial(correa_incorrecta[1]))

            correa_correcta_codigo.append(correa_correcta[2])
            correa_correcta_descripcion.append(retornadescripcion(correa_correcta[2]))
            correa_correcta_fecha_compra_maestra.append(sucursal.fecha_compra(correa_correcta[2]))
            correa_correcta_fecha_venta_maestra.append(sucursal.fecha_venta(correa_correcta[2]))
            correa_correcta_inv_bodega.append(sucursal.inventario_bodega(correa_correcta[2]))
            correa_correcta_inv_matriz.append(sucursal.inventario_matriz(correa_correcta[2]))
            correa_correcta_inv_serena.append(sucursal.inventario_laserena(correa_correcta[2]))
            correa_correcta_inv_industrial.append(sucursal.inventario_industrial(correa_correcta[2]))
        
        else:
            codigo = correa_incorrecta[0]
            if(codigo in correa_correcta[0]):
                
                correa_incorrecta_codigo.append(correa_incorrecta[1])
                correa_incorrecta_descripcion.append((correa_incorrecta[0]))
                correa_incorrecta_fecha_compra_maestra.append(sucursal.fecha_compra(correa_incorrecta[1]))
                correa_incorrecta_fecha_venta_maestra.append(sucursal.fecha_venta(correa_incorrecta[1]))
                correa_incorrecta_inv_bodega.append(sucursal.inventario_bodega(correa_incorrecta[0]))
                correa_incorrecta_inv_matriz.append(sucursal.inventario_matriz(correa_incorrecta[0]))
                correa_incorrecta_inv_serena.append(sucursal.inventario_laserena(correa_incorrecta[0]))
                correa_incorrecta_inv_industrial.append(sucursal.inventario_industrial(correa_incorrecta[0]))

                if(len(correa_correcta)==2):
                    correa_correcta_codigo.append(correa_correcta[len(correa_correcta)-1])
                    correa_correcta_descripcion.append(correa_correcta[0])
                    correa_correcta_fecha_compra_maestra.append(sucursal.fecha_compra(correa_correcta[1]))
                    correa_correcta_fecha_venta_maestra.append(sucursal.fecha_venta(correa_correcta[1]))
                    correa_correcta_inv_bodega.append(sucursal.inventario_bodega(correa_correcta[1]))
                    correa_correcta_inv_matriz.append(sucursal.inventario_matriz(correa_correcta[1]))
                    correa_correcta_inv_serena.append(sucursal.inventario_laserena(correa_correcta[1]))
                    correa_correcta_inv_industrial.append(sucursal.inventario_industrial(correa_correcta[1]))
                
                   
        
        i=i+1
           

correas_corregido = pandas.DataFrame(list(zip(correa_incorrecta_codigo,correa_incorrecta_descripcion,correa_incorrecta_fecha_compra_maestra,correa_incorrecta_fecha_venta_maestra,correa_incorrecta_inv_bodega,correa_incorrecta_inv_matriz,correa_incorrecta_inv_serena,correa_incorrecta_inv_industrial,correa_correcta_codigo,correa_correcta_descripcion,correa_correcta_fecha_compra_maestra,correa_correcta_fecha_venta_maestra,correa_correcta_inv_bodega,correa_correcta_inv_matriz,correa_correcta_inv_serena,correa_correcta_inv_industrial)), columns =nombre_columnas)
correas_corregido.to_csv(r'./results/Correccion de correas.csv', header=nombre_columnas, index=False, sep=',', mode='w')
print("Archivo creado")