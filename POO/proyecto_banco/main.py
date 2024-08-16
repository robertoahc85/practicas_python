from cuenta_ahorro import CuentaAhorro
def main():
    cuenta1= CuentaAhorro("Roberto Hernandez",1000)
    print(f"El nombre del titula es {cuenta1.titular}")
    print(f"El saldos es: ${cuenta1.saldo}")
    print(f"La Tasa de interes es: ${cuenta1.tasa_interes * 100}%")
    
    cuenta1.depositar(500)
    cuenta1.retirar(200)
    cuenta1.aplicar_interes()
    
    print(f"El saldos es: ${cuenta1.saldo}")

if __name__ == "__main__":
    main()