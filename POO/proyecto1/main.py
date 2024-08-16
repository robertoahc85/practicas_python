from coche import Coche

def main():
    mi_coche = Coche("Toyota","Yaris",4)
    mi_coche.arrancar()
    mi_coche.abrir_puertas()
    mi_coche.detener()

if __name__ == "__main__":
    main()