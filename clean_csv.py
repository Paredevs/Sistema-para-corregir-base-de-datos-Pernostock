import csv,time

errors = []

def busca_duplicados(columna):
   # mylist = [5, 3, 5, 2, 1, 6, 6, 4] # 5 & 6 are duplicate numbers.
# find the length of the list
    print(len(columna))
    # create a set from the list
    myset = set(columna)
    # find the length of the Python set variable myset
    print(len(myset))
    # compare the length and print if the list contains duplicates
    if len(columna) != len(myset):
        print("duplicates found in the list")
    else:
        print("No duplicates found in the list")
def comprueba_codigo(codigo):
   
    if len(codigo)>8  :
        time.sleep(1)
        print("\nCodigo: ",codigo)  ##mprimir el codigo erroneo
        respuesta=input("¿Corregir valor? (s/n):")
        if(respuesta=="s"):
            codigo_antiguo=codigo
            codigo=input("\nIngrese el nuevo valor:")
            print("Antiguo codigo",codigo_antiguo,"\nNuevo codigo: ",codigo)
       ## print("ERROR: El codigo es mayor a 8 digitos")
        return True, codigo
    else:
        return False
def comprueba_descripcion(descripcion):
    pass
def comprueba_cod_barra(codigo_barra):

    if(codigo_barra.isnumeric()):
       return True 
    return False
       
def recorre_archivo(campo):
    
    file =  open ("./productos 2023 Arreglado python.csv","r")
    csvreader = csv.reader(file, delimiter=',')
    for row in csvreader:
        match campo:
            case 0: comprueba_codigo(row[0])
            case 1: comprueba_descripcion(row[1])
            case 2: 
                    if(comprueba_cod_barra(row[2])):
                        print("Codigo de barra: ",row[2])
                       # output.write(row)
                    else:
                         print("ERROR: El codigo de barra no es numerico :",    row[2], "Codigo: ",row[0])
                         input("Presione enter para continuar")
                         
            case 3: comprueba_UM(row[3])
            case 4: comprueba_grupo(row[4])
            case 5: comprueba_subgrupo(row[5])
            case 6: comprueba_parte(row[6])
            case 7: comprueba_origen(row[7])
            case 8: comprueba_precio_venta(row[8])
            case 9: comprueba_fecha_ult_compra(row[9])
            case 10: comprueba_valor_ult_compra(row[10])
            case 11: comprueba_fecha_ult_venta(row[11])
            case 12: comprueba_valor_ult_venta(row[12])
            case 13: comprueba_ultimo_proveedor(row[13])
            case 14: comprueba_stock_casa_matriz(row[14])
            case 15: comprueba_stock_la_serena(row[15])
            case 16: comprueba_stock_barrio_industrial(row[16])
            case 17: comprueba_stock_bodega_central(row[17])
            case 18: comprueba_total_empresa(row[18])
            case _: print("Opcion invalida")
        
       # time.sleep(1)
    file.close()
def comprueba_UM(um):
    if(um.isnumeric()==False):
        return True
    return False

    
lista = []    
contador=1
indice=1
campo= int(input("Ingrese el campo a verificar: \n0)Codigo\n1)Descripcion\n2)Cod.Barra\n3)U.M\n4)Grupo\n5)Sub grupo\n6)Parte\n7)Origen\n8)Precio Venta\n9)Fecha Ult.Compra\n10)Valor Ult.Compra\n11)Fecha Ult.Venta\n12)Valor Ult.Venta\n13)Ultimo.Proveedor\n14)Stock Casa matriz\n15)Stock La Serena\n16)Stock barrio Industrial\n17)Stock Bodega Central\n18)Total Empresa\nNumero de campo:"))
recorre_archivo(campo)

   



        #time.sleep(1)
        # if(comprobar_codigo(row[0])):
        #     errors.append(contador)
        #     contador=contador+1
        #     indice=indice+1
        # if(comprueba_descripcion(row[1])):
        #     pass
        # #print("indice :",indice,"Codigo: ",row[0]," Descripcion: ",row[1]," C.B: ",row[2]," U.M: ",row[3],)
        # if(comprueba_UM(row[3])):
        #     contador=contador+1
        #     errors.append(contador)
        #     print("Codigo: ",row[0]," U.M: ",row[3],)
        # indice=indice+1
        # #recorre_archivo(3)
        #lista.append(row[0])
        
#busca_duplicados(lista)
#print("Errores: ",len(errors))


file.close()