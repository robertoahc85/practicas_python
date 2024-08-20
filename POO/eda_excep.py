class EdainvalidadError(Exception):
    pass
    def verificarEdad(edad):
        if edad < 18: 
            raise ValueError("Deber ser mayor de 18 anios para registrarse")
        return "Registro Completo"
    try:
        mensaje = verificarEdad(15)
        print(mensaje)
    except  ValueError as e:
        print(f"{e}")

    