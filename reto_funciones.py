# Crea una función llamada calcular_precio_final que reciba dos parámetros:
 
# precio_inicial: el precio original del producto.
# descuento: el porcentaje de descuento a aplicar (un número entre 0 y 100).
# La función debe devolver el precio final del producto después de aplicar el descuento.
 
# Asegúrate de que la función maneje correctamente los siguientes casos:
 
# Si el descuento es 0, el precio final debe ser igual al precio inicial.
# Si el descuento es 100, el precio final debe ser 0.
# El descuento no puede ser negativo ni mayor que 100; en esos casos, la función debe devolver el mensaje "Descuento inválido".
# Escribe un código que solicite al usuario que ingrese el precio inicial y el descuento, y luego muestre el precio final utilizando la función calcular_precio_final












def calcular_precio_final(precio_inicial, descuento):
    # Validar que el descuento esté en el rango permitido
    if descuento < 0 or descuento > 100:
        return "Descuento inválido"
    
    # Calcular el precio final aplicando el descuento
    precio_final = precio_inicial * (1 - descuento / 100)
    return precio_final


# Solicitar al usuario los valores de entrada
precio = float(input("Ingresa el precio inicial del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

# Calcular y mostrar el precio final
resultado = calcular_precio_final(precio, descuento)
print("El precio final del producto es:", resultado)
