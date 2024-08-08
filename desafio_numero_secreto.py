
# Desafío: Adivina el Número Secreto
# Objetivo: Implementar un juego en Python donde el usuario debe adivinar un número secreto entre 1 y 100. 
# El programa debe indicar si el número ingresado es mayor o menor al número secreto y continuar preguntando hasta que el usuario lo adivine.

# Instrucciones:
# Generar un número secreto aleatorio entre 1 y 100.
# Pedir al usuario que adivine el número secreto.
# Comparar el número ingresado por el usuario con el número secreto:
# Si el número ingresado es mayor que el número secreto, mostrar el mensaje: "El número secreto es menor. Intenta de nuevo."
# Si el número ingresado es menor que el número secreto, mostrar el mensaje: "El número secreto es mayor. Intenta de nuevo."
# Si el número ingresado es igual al número secreto, mostrar el mensaje: "¡Felicidades! Has adivinado el número secreto." y terminar el juego.
# Continuar pidiendo al usuario que adivine hasta que acierte el número secreto.


















import random
numero_secreto = random.randint(1, 100)
adivinado = False






while not adivinado:
    intento = int(input("Adivina el número (entre 1 y 100): "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        adivinado = True
    elif intento < numero_secreto:
        print("El número es mayor. Intenta nuevamente.")
    else:
        print("El número es menor. Intenta nuevamente.")
        
        

 
#usando while else

numero_secreto = random.randint(1, 100)
intentos_restantes = 5

while intentos_restantes > 0:
    intento = int(input("Adivina el número secreto entre 1 y 100: "))
    intentos_restantes -= 1

    if intento > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
else:
    print(f"Lo siento, no has adivinado el número secreto. Era {numero_secreto}.")
       
       
#usando for

for _ in range(5):
    intento = int(input("Adivina el número secreto entre 1 y 100: "))
    
    if intento > numero_secreto:
        print("El número secreto es menor. Intenta de nuevo.")
    elif intento < numero_secreto:
        print("El número secreto es mayor. Intenta de nuevo.")
    else:
        print("¡Felicidades! Has adivinado el número secreto.")
        break
else:
    print(f"Lo siento, no has adivinado el número secreto. Era {numero_secreto}.")      
       