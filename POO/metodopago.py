from abc import  ABC,abstractmethod
class  MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self,cantidad):
        pass
 
#clase hija  que procesa pago para tarjeta de credito
class Pago_Tarjeta_Credito(MetodoPago):
    def procesar_pago(self,cantidad):
        print(f"Procesando un pago de la ${cantidad} con tarjeta de credito ")   
    def validaNumeroTarjeta(self,numeroTarjeta):
        print(f"Validando numero tarjeta de{numeroTarjeta}")  
            
#clase hija  que procesa pago con Paypal;
class Pago_Paypal(MetodoPago):
    def procesar_pago(self,cantidad):
        print(f"Procesando un pago con Paypal de ${cantidad}")
    def validanConexionApi(self):
        print(f"Validando conexion con Api")   
 #clase hija  que procesa pago con Criptomoneda;       
class PagoCriptomoneda(MetodoPago):
    def procesar_pago(self,cantidad):
        print(f"Procesando un pago con Criptomoneda de la ${cantidad}")       

def realizar_pago(metodo_pago,cantidad):
    metodo_pago.procesar_pago(cantidad)   
       
#main
pago1 = Pago_Tarjeta_Credito()
pago2 = Pago_Paypal()
pago3 = PagoCriptomoneda()
pago1.validaNumeroTarjeta("212112")
realizar_pago(pago1,100)
realizar_pago(pago2,500)
realizar_pago(pago3,700)


    