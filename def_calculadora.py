#metodos
def sumar(a,b):
    return a+b
def resta(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    return a/b
def imprimir_resultado(a,b,resultado):
    print(f"El Resulado de la Resta de: {a} y {b} es: {resultado}")
    
def solicitar_numeros():
    num1=float(input("ingresa el primer numero: "))
    num2=float(input("ingresa el segundo numero: "))
    return num1,num2

def calculadora():
    print("------Bienvenido a la Calculadora 0077------")
    while True:
        print("\nSelecione una operacion ")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")
        opcion = int(input("Ingresa tu opcion del(1-5)"))
        
        if opcion == 1 :
            num1,num2= solicitar_numeros()
            resultado=sumar(num1,num2)
            imprimir_resultado(num1,num2,resultado)
        elif opcion ==2:
            num1,num2= solicitar_numeros()
            resultado=resta(num1,num2)
            imprimir_resultado(num1,num2,resultado)
        elif opcion ==3:
            num1,num2= solicitar_numeros()
            resultado=multiplicar(num1,num2)
            imprimir_resultado(num1,num2,resultado)
        elif opcion ==4:
            num1,num2= solicitar_numeros()
            resultado=dividir(num1,num2)
            imprimir_resultado(num1,num2,resultado)
        elif opcion == 5:  
            print("Hasta la proxima")  
            break  
        else: print("Opcion no valida")    
#Main
calculadora()


