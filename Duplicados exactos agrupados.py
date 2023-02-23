import funciones,pandas,time
from tqdm import tqdm
 
#Programa creado para buscar duplicados exactos en todas las bases de datos (Maestra, Bodega, Matriz, La Serena, Industrial) y agruparlos por codigo de producto

def ordenaResultados():

    print("Ordenando resultados...")
    for key, value in tqdm(dic_duplicados.items()): #Recorremos el diccionario de duplicados a través de sus descripciones y codigos como valores
        duplicados_unicos.append(key)
        lista = ''
        string_compra = ''
        string_venta = ''
        for i in value:
            lista = lista +"-"+ i + '\n---------------\n'
            for codigo_de_compra,fecha_compra_actual in todo_fecha_compra.items():
                if(i == codigo_de_compra):
                    string_compra = string_compra  + fecha_compra_actual+'\n---------------\n'
            for codigo_de_venta,fecha_venta_actual in todo_fecha_venta.items():
                if(i == codigo_de_venta):
                    string_venta = string_venta  + fecha_venta_actual+'\n---------------\n'
        
        lista_venta.append(string_venta)
        lista_compra.append(string_compra)
        lista_duplicados.append(lista)


   
                                        #Casa Matriz
        #--------------------------------------------------------------------------

        string_matriz = ''
        for codigo_duplicado in value:
            for codigo_de_stock,stock_actual in todo_stock_matriz.items():
                if(codigo_duplicado == codigo_de_stock):
                    string_matriz = string_matriz  + stock_actual+'\n---------------\n'

        lista_stock_matriz.append(string_matriz)

        string_matriz = ''
        for codigo_duplicado in value:
            for codigo_de_inventario,inventario_actual in todo_inv_matriz.items():
                if(codigo_duplicado == codigo_de_inventario):
                    string_matriz = string_matriz  + inventario_actual+'\n---------------\n'

        lista_inv_matriz.append(string_matriz)

        string_matriz = ''
        for codigo_duplicado in value:
            for codigo_de_compra,fecha_compra_actual in todo_fecha_compra.items():
                if(codigo_duplicado == codigo_de_compra):
                    string_matriz = string_matriz  + fecha_compra_actual+'\n---------------\n'
        #lista_compra_matriz.append(string_matriz)

        string_matriz = ''

        for codigo_duplicado in value:
            for codigo_de_venta,fecha_venta_actual in todo_fecha_venta.items():
                if(codigo_duplicado == codigo_de_venta):
                    string_matriz = string_matriz  + fecha_venta_actual+'\n---------------\n'
       # lista_venta_matriz.append(string_matriz)

        
                                    #La Serena
        #--------------------------------------------------------------------------

       
        string_laserena = ''
        for codigo_duplicado in value:
            for codigo_de_stock,stock_actual in todo_stock_laserena.items():
                if(codigo_duplicado == codigo_de_stock):
                    string_laserena = string_laserena  + stock_actual+'\n---------------\n'

        lista_stock_laserena.append(string_laserena)

        string_laserena = ''
        for codigo_duplicado in value:
            for codigo_de_inventario,inventario_actual in todo_inv_laserena.items():
                if(codigo_duplicado == codigo_de_inventario):
                    string_laserena = string_laserena  + inventario_actual+'\n---------------\n'
        
        lista_inv_laserena.append(string_laserena)

        string_laserena = ''
        for codigo_duplicado in value:
            for codigo_de_compra,fecha_compra_actual in todo_fecha_compra.items():
                if(codigo_duplicado == codigo_de_compra):
                    string_laserena = string_laserena  + fecha_compra_actual+'\n---------------\n'
        #lista_compra_laserena.append(string_laserena)

        string_laserena = ''
        for codigo_duplicado in value:
            for codigo_de_venta,fecha_venta_actual in todo_fecha_venta.items():
                if(codigo_duplicado == codigo_de_venta):
                    string_laserena = string_laserena  + fecha_venta_actual+'\n---------------\n'
       # lista_venta_laserena.append(string_laserena)
        
                                    #Industrial
        #--------------------------------------------------------------------------
        

        string_industrial = ''
        for codigo_duplicado in value:
            for codigo_de_stock,stock_actual in todo_stock_industrial.items():
                if(codigo_duplicado == codigo_de_stock):
                    string_industrial = string_industrial  + stock_actual+'\n---------------\n'
        
        lista_stock_industrial.append(string_industrial)

        string_industrial = ''
        for codigo_duplicado in value:
            for codigo_de_inventario,inventario_actual in todo_inv_industrial.items():
                if(codigo_duplicado == codigo_de_inventario):
                    string_industrial = string_industrial  + inventario_actual+'\n---------------\n'
        
        lista_inv_industrial.append(string_industrial)

        string_industrial = ''
        for codigo_duplicado in value:
            for codigo_de_compra,fecha_compra_actual in todo_fecha_compra.items():
                if(codigo_duplicado == codigo_de_compra):
                    string_industrial = string_industrial  + fecha_compra_actual+'\n---------------\n'
        #ista_compra_industrial.append(string_industrial)

        string_industrial = ''
        for codigo_duplicado in value:
            for codigo_de_venta,fecha_venta_actual in todo_fecha_venta.items():
                if(codigo_duplicado == codigo_de_venta):
                    string_industrial = string_industrial  + fecha_venta_actual+'\n---------------\n'
        #lista_venta_industrial.append(string_industrial)

                                    #Bodega central
        #--------------------------------------------------------------------------


        string_bodega = ''
        for codigo_duplicado in value:
            for codigo_de_stock,stock_actual in todo_stock_bodega.items():
                if(codigo_duplicado == codigo_de_stock):
                    string_bodega = string_bodega  + stock_actual+'\n---------------\n'

        lista_stock_bodega.append(string_bodega)

    
        string_bodega = ''

        for codigo_duplicado in value:
            for codigo_de_inventario,inventario_actual in todo_inv_bodega.items():
                if(codigo_duplicado == codigo_de_inventario):
                    string_bodega = string_bodega  + inventario_actual+'\n---------------\n'

        lista_inv_bodega.append(string_bodega)
        

       
        

        #--------------------------------------------------------------------------

       
if(isinstance(funciones.compruebaBasededatos(), str)):  #Verifica si existen las bases de datos
    print(funciones.compruebaBasededatos()) #Imprime cual base de datos no existe
    input("Presione enter para salir...")
    exit()

    

duplicados_unicos,grupo,subgrupo,lista_duplicados = [],[],[],[]   #Listas para guardar los resultados
lista_stock_bodega,lista_stock_matriz,lista_stock_laserena,lista_stock_industrial = [],[],[],[]
lista_inv_bodega,lista_inv_matriz,lista_inv_laserena,lista_inv_industrial = [],[],[],[]
lista_compra = []
lista_venta = []
fecha_compra = []
fecha_venta = []
base_datos= int(input("Ingrese el nombre de la base de datos a buscar: \n1) Maestra 2) Bodega central 3) Casa matriz 4) La Serena 5) Industrial: "))
print("Buscando duplicados exactos en la base de datos")
if(base_datos == 1): #Busca los duplicados en la maestra
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.MAESTRA_PATH,1))
    FILE_NAME = "MAESTRA Duplicados exactos agrupados.xlsx"
elif(base_datos == 2):  #Busca los duplicados en la bodega central
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.BODEGA_PATH,2))
    FILE_NAME = "BODEGA CENTRAL Duplicados exactos agrupados.csv.xlsx"
elif(base_datos == 3):  #Busca los duplicados en la casa matriz
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.MATRIZ_PATH,2))
    FILE_NAME = "CASA MATRIZ Duplicados exactos agrupados.xlsx"
elif(base_datos == 4):   #Busca los duplicados en la sucursal la serena
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.LASERENA_PATH,2))
    FILE_NAME = "LA SERENA Duplicados exactos agrupados.xlsx"
elif(base_datos == 5):   #Busca los duplicados en la sucursal  barrio industrial
    dic_duplicados = dict(funciones.duplicadosExactosAgrupados(funciones.INDUSTRIAL_PATH,2))
    FILE_NAME = "INDUSTRIAL Duplicados exactos agrupados.xlsx"
else:
    print("Opcion invalida")
    exit()
    
print("Cantidad de productos unicos duplicados: ",len(dic_duplicados))
total_duplicados = sum(len(l) for l in list(dic_duplicados.values()))
print("Cantidad de descripciones duplicadas: ",total_duplicados)

todo_stock_matriz = dict(funciones.getStock()[0])
todo_stock_laserena = dict(funciones.getStock()[1])
todo_stock_industrial = dict(funciones.getStock()[2])
todo_stock_bodega = dict(funciones.getStock()[3])

todo_inv_matriz = dict(funciones.guarda_inventario_matriz())
todo_inv_laserena = dict(funciones.guarda_inventario_laserena())
todo_inv_industrial = dict(funciones.guarda_inventario_industrial())
todo_inv_bodega = dict(funciones.guarda_inventario_bodega())

todo_fecha_compra= dict(funciones.getCompra())
todo_fecha_venta= dict(funciones.getVenta())


time.sleep(2)
ordenaResultados()



try:
    funciones.verificaCarpeta()  #Veriiica si existe la carpeta de resultados
    resultado = pandas.DataFrame(list(zip(duplicados_unicos,lista_duplicados,lista_stock_bodega,lista_inv_bodega,lista_stock_matriz,lista_inv_matriz,lista_stock_laserena,lista_inv_laserena,lista_stock_industrial,lista_inv_industrial,lista_compra,lista_venta)), columns =["Descripcion","Duplicados","Stock Bodega","Inventario Bodega","Stock Matriz","Inventario Matriz","Stock La Serena","Inventario La Serena","Stock Industrial","Inventario Industrial","Ult. compra","Ult. venta"])
    #resultado.to_csv(r''+funciones.RESULTS_PATH+FILE_NAME, header=True, index=False, sep=',', mode='w')
    resultado.to_excel(funciones.RESULTS_PATH+FILE_NAME, header=True, index=False)
except Exception as e: 
    print("Error al generar el archivo ",FILE_NAME)
    print(e)
    input("Presione enter para continuar...")
    exit()
print("Archivo generado correctamente en "+funciones.RESULTS_PATH)
input("Presione enter para salir")
exit()