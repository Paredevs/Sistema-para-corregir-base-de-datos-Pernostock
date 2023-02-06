numero =str(input("Ingrese un numero: "))
while(len(numero)>8 or len(numero)<0 or numero.isnumeric()==False):
    print("Numero invalido")
    numero =str(input("Ingrese un numero: "))
print("Numero valido")
print("Numero: ",numero)