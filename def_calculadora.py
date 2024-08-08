#metodos
def sumar(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b

def calculadora():
    print("------Bienvenido a la Calculadora 0077------")
    while True:
        print("\nSelecione una operacion ")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")
        opcion = input("Ingresa tu opcion del(1-5)") 
        
        if opcion ==1:
            num1=float(input("ingresa el primer numero"))
            num2=float(input("ingresa el segundo numero"))
            resultado=sumar(num1,num2)
            print(f"El Resulado de la Suma de: {num1} y {num2} es: {resultado}")
        elif opcion ==2:
            num1=float(input("ingresa el primer numero"))
            num2=float(input("ingresa el segundo numero"))
            resultado=resta(num1,num2)
            print(f"El Resulado de la Resta de: {num1} y {num2} es: {resultado}")
        elif opcion ==3:
            num1=float(input("ingresa el primer numero"))
            num2=float(input("ingresa el segundo numero"))
            resultado=multiplicar(num1,num2)
            print(f"El Resulado de la Multiplicacion de: {num1} y {num2} es: {resultado}") 
        elif opcion ==4:
            num1=float(input("ingresa el primer numero"))
            num2=float(input("ingresa el segundo numero"))
            resultado=dividir(num1,num2)
            print(f"El Resulado de la Division de: {num1} y {num2} es: {resultado}")
        elif opcion == 5:  
            print("Hasta la proxima")  
            break  
        else: print("Opcion no valida")    
#Main
calculadora()


