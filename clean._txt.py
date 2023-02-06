import time

output = open("./productos 2023 Arreglado python.csv","w")
with open("./productos 2023 Arreglado.csv","r") as archivo:
    for linea in archivo:
        codigo=linea[0:10]
        if(codigo[0]=='"'):
            output.write(linea[1:])
            #print(linea[1:])
          #  errors.append(contador)
           # time.sleep(1)
        else:
            output.write(linea)
#print("Errores: ",len(errors)) 
archivo.close()
output.close()

errors = []
contador=0
archivo_nuevo = open("./productos 2023 Arreglado python.csv","r")
for linea in archivo_nuevo:
        codigo=linea[0:10]
        if(codigo[0]=='"'):
            #print(linea[1:])
            contador=contador+1
            errors.append(contador)
           # time.sleep(1)
print("Errores: ",len(errors)) 
     
