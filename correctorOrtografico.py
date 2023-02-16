import csv,time,pandas,re,sucursal,numpy as np
from spellchecker import SpellChecker
from tqdm import tqdm
from tabulate import tabulate


spanish = SpellChecker(language='es')


    

def errores_ortograficos(descripcion):
    

   # x = re.search('[B|V]', descripcion)
    x = re.findall("[{}¿?]|ÑT|EMBRAGE|UUU|ISQ|AAAA|BBB|CCCC|EEE|HHKG|LLLL|(^PP5|^PP\d$|PPP\d$|PPPP$)|QQQ|RRRR|LALVE|SSS|^XXX|INMIVI|MAUSE|^MASA|(PARACHOQ|PARACH|PARACHOE|PARACHO)$|([^a-zA-Z]PARACH[^a-zA-Z])|5NJ|FUELLE|DSIC|DSIT|SDF|SASD|YYY|^LB$|VACA|DI9S|^A$|^H$|PEDIDO|DIDP|DIS`|GRT|NWU|80X40X15X3MM", descripcion)
    #x = re.findall("^CORREA \dPK.*|(^CORREA V.* \dPK \d\d\d\d)",descripcion)
    if(x):
        print("CORREAS: ",row[0]," D:",descripcion)
       # time.sleep(0.5)


        return 1

    #AAAA|BBB|CCCC
    # if(x):
    #     pass
    #     print("B o V: ",row[0]," D:",descripcion)
    # x = re.search('(TAMOR|V)', descripcion)
    # if(x):
        
    #    # print("TAM*OR: ",row[0]," D:",descripcion)
    #     return 1
    return 0



codigo,descripcion,tipo_error  = [],[],[]
inventario_industrial,inventario_laserena,inventario_matriz,inventario_bodega = [],[],[],[]
fecha_compra_maestra,fecha_venta_maestra = [],[]
 

inv_industrial = dict(sucursal.guarda_inventario_industrial())
inv_laserena = dict(sucursal.guarda_inventario_laserena())
inv_matriz = dict(sucursal.guarda_inventario_matriz())
inv_bodega = dict(sucursal.guarda_inventario_bodega())

palabras_pk = []
palabras_correa = []
una_palabra =[]



contador = 0
#guarda_codigos()


# maestra =  open ("./database/Maestra.csv","r")
maestra =  open ("./database/maestra 8-2-23.csv","r")
csvreader = csv.reader(maestra, delimiter=',')


for row in tqdm(csvreader):

        if(row[1]=='' or row[1].isspace()):
           # print("La descripcion esta vacia")
            codigo.append(row[0])   #Se añade codigo
            descripcion.append('Vacio')
            tipo_error.append("Descripcion vacia")
            inventario_matriz.append(inv_matriz.get(row[0]))
            inventario_bodega.append(inv_bodega.get(row[0]))
            inventario_laserena.append(inv_laserena.get(row[0]))
            inventario_industrial.append(inv_industrial.get(row[0]))
            
            fecha_compra_maestra.append(sucursal.fecha(row[9]))
            fecha_venta_maestra.append(sucursal.fecha(row[11]))
            contador= contador + 1
            
        else:
            descripcion_sin_espacios = str(row[1]).replace(" ","")
            #print(descripcion_acortada)
            #time.sleep(1)
            contador = contador + errores_ortograficos(row[1].rstrip())
           
            #
            # x = re.search('^([OMBILLA]+)|OMBILLA$', txt)
            
    
            if(descripcion_sin_espacios.isdigit()):
          #      print("La descripcion es un numero", descripcion_sin_espacios, "Codigo: ",row[0])
           #     time.sleep(1)
                codigo.append(row[0])
                descripcion.append(row[1])
                tipo_error.append("Solo numeros")
                inventario_matriz.append(inv_matriz.get(row[0]))
                inventario_bodega.append(inv_bodega.get(row[0]))
                inventario_laserena.append(inv_laserena.get(row[0]))
                inventario_industrial.append(inv_industrial.get(row[0]))
            
                
                fecha_compra_maestra.append(sucursal.fecha(row[9]))
                fecha_venta_maestra.append(sucursal.fecha(row[11]))
                contador= contador + 1
                
            else:
                descripcion_separada = str(row[1]).split()
              #  print("Descripcion separada",descripcion_separada)
               # time.sleep(1)
                
                
                    
                    
                if(len(descripcion_separada)==1 and len(descripcion_separada[0])>3 and descripcion_separada[0][0].isdigit() and  descripcion_separada[0][1]=="P"):
                        palabras_pk.append(descripcion_separada)
                        # print(descripcion_separada)
                        # time.sleep(1)

                        #print("La descripcion es una correa:", descripcion_separada)
                     # print("separada por - : ",descripcion_separada[0].split("-"))
                
                matches = ["CORREA","PK"]
                if any([x in row[1] for x in  matches]):
                   # print("La descripcion es una correa con PK:", descripcion_separada)
                    pass
                if(len(descripcion_separada) == 1):   #Verifica si la descripcion es una sola palabra
                 #   print(descripcion_separada)  #imprime descripcion de una sola palabra
                    #time.sleep(1)
                    
                    # word = descripcion_separada[0]
                    # print("Descripcion separada",descripcion_separada[0],"Recomendacion ",spanish.candidates(word))
                    # time.sleep(1)
                    # una_palabra.append(row[1])
                    pass
                
                if(((descripcion_separada[0].isalpha() and len(descripcion_separada[0]) == 1) or  (descripcion_separada[0].isalpha() and len(descripcion_separada[0]) == 2)    )  and len(descripcion_separada) == 2 and ((row[9] == '' and row[11] == '') or (row[9] != '' and row[11] == '') or (row[9] == '' and row[11] != ''))):
                    #print("fecha ultima compra:",row[9],"fecha ultima venta:" ,row[11])
                    
                    #print("La descripcion empieza con una letra:", row[1])
                    codigo.append(row[0])
                    descripcion.append((row[1]).rstrip())
                    tipo_error.append("Letras y numeros")
                    inventario_matriz.append(inv_matriz.get(row[0]))
                    inventario_bodega.append(inv_bodega.get(row[0]))
                    inventario_laserena.append(inv_laserena.get(row[0]))
                    inventario_industrial.append(inv_industrial.get(row[0]))
            
                    fecha_compra_maestra.append(sucursal.fecha(row[9]))
                    fecha_venta_maestra.append(sucursal.fecha(row[11]))
                    contador= contador + 1
                    
    
                
                   
                

print("Total descripciones con errores ortograficos: ",contador    )                          
maestra.close()



palabras_vacias = pandas.DataFrame(list(zip(codigo,tipo_error,descripcion,inventario_industrial,inventario_laserena,inventario_matriz,inventario_bodega,fecha_compra_maestra,fecha_venta_maestra)), columns =["Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega","Ult. fecha compra","Ult.fecha venta"])
palabras_vacias.to_csv(r'./results/Errores ortograficos.csv', header={"Codigo",'Tipo error', 'Descripcion',"I.Industrial","I.La Serena","I.Matriz","I.Bodega","Ult. fecha compra","Ult.fecha venta"}, index=True, sep=',', mode='w')
una_palabra= pandas.DataFrame(list(zip(una_palabra)), columns =["Descripcion"])
una_palabra.to_csv(r'./results/Descripciones de una palabra.csv', header={"Descripcion"}, index=True, sep=',', mode='w')
print("Archivo generado \n")
#table= tabulate(palabras_vacias, headers = 'keys', tablefmt = 'psql')   #Para crear tabla
#print(table)
#print("Palabras que empiezan con numero: \n",tabulate(palabras_empieza_numero, headers = 'keys', tablefmt = 'github'))
