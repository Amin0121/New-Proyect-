import hashlib, binascii
import getpass

class Cuenta():
    def __init__(self, usuario, clave):
        self.usuario = usuario
        self.clave = clave
    
class inicio():
    def __init__(self):
        self.cuentas = []

    def agregarCuenta(self):
        nombreUsuario = input('Ingresa el nombre del usuario:')
        nombreClave = getpass.getpass('Ingresa la clave de cuenta:')

        hash = hashlib.pbkdf2_hmac('sha256', nombreClave.encode(), b'hjhns', 10000)

        nuevaCuenta = Cuenta(nombreUsuario, binascii.hexlify(hash))
        self.cuentas.append(nuevaCuenta)

    def verCuenta(self):
        for recorer in self.cuentas:
            print ("Usuario:", recorer.usuario,'\nClave:', recorer.clave)
    


inicio1 = inicio()



while True:

    print('\n\t MENU \n'
    '1. Crear Cuenta\n' 
    '2. Ver la Cuenta\n' 
    '3. Salir')

    eleccion = input('Seleccionar una opcion:')

    if (eleccion == '1'):
        print('\n\t Creacion de la Cuenta \n')
        inicio1.agregarCuenta()

    elif(eleccion == '2'):
        print('\n\t Datos de la cuenta \n')
        inicio1.verCuenta()
            
    elif(eleccion == '3'):
        print('\n \t Gracias por su visita \n')
        break
    
    else:
        print('\n \t OPCION INCORRECTA PRUEVA OTRA VEZ \n')