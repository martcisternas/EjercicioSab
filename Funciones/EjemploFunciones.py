import funcionesDetalle as fn
#from funcionesDetalle import sumar

#Linea ppal 
fn.sumarDosNumeros()

res = fn.sumar(4,5)
print(res)

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
res = fn.sumar(num1,num2)
print("La suma es: ", res)

def resta(a,b):
    '''Esta funcion permite restar dos números
    ingresados por parametros'''
    resta = a - b
    return resta

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
res = resta(num1,num2)
print("La resta es :",res)

def RestarDosNumeros():
    '''Esta funcion permite restar dos números
    ingresados por parametros'''

    num1 = int(input("Ingrese numero 1: "))
    num2 = int(input("Ingrese numero 2: "))

    resta = num1 - num2

    print(f"La resta de {num1} - {num2} es = {resta}")

RestarDosNumeros()