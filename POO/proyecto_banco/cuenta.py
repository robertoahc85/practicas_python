class Cuenta:
    def __init__(self,titular, saldo=0):
        self._titular=titular #atributo protegido
        self._saldo=saldo #atributo protegido
        
    @property
    def titular(self):
        return self._titular
    @property
    def saldo(self):
        return self._saldo 
    
    @saldo.setter
    def saldo(self,cantidad):
        if cantidad < 0:
            print (" La cantidad no puede ser negativo o 0")
        else:
            self._saldo = cantidad
         
    def depositar(self,cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            print (f"se ha depositado ${cantidad}.Su nuevo saldo:${self._saldo}")
        else:
            print ("La cantidad a depositar debe ser positiva")
            
    def retirar(self,cantidad):
        if 0  < cantidad <= self._saldo:
            self._saldo -= cantidad
            print (f"se ha retirado la ${cantidad}.Su nuevo saldo:${self._saldo}")
        else:
            print("Fondos insuficientes")  