from cuenta import Cuenta
class CuentaAhorro(Cuenta):
    def __init__(self,titular,saldo=0,tasa_interes=0.02):
        super().__init__(titular,saldo)
        self._tasa_interes = tasa_interes
        
    @property
    def tasa_interes(self): 
        return self._tasa_interes 
    
    @tasa_interes.setter
    def tasa_interes(self,tasa): 
        if tasa < 0:
            print("La tasa de interes no puede ser negativa")
        else:
            self._tasa_interes = tasa 
              
    def aplicar_interes(self):
        interes = self._saldo * self._tasa_interes
        self._saldo += interes
        print(f"Interes Aplicado ${interes}, tu nuevo saldo es: ${self._saldo}")
                