class Cliente:
    def __init__(self, nombre, apellido, pin=None):
        self.nombre = nombre
        self.apellido = apellido
        self.pin = pin
        self.cuentas = []

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

    def obtener_cuentas(self):
        return self.cuentas


class CuentaBancaria:
    nombre_banco = 'Banco de la UAX'

    def __init__(self, numero_cuenta, cliente, moneda='EUR'):
        self.numero_cuenta = numero_cuenta
        self.cliente = cliente
        self.moneda = moneda
        self.saldo = 0
        cliente.cuentas.append(self)

    def ingresar(self, cantidad):
        if not 0 < cantidad < float('inf'):
            return False
        self.saldo = round(self.saldo + cantidad, 2)
        return True

    def retirar(self, cantidad):
        if not 0 < cantidad <= self.saldo:
            return False
        self.saldo = round(self.saldo - cantidad, 2)
        return True

    def obtener_saldo(self):
        return f'{self.saldo:.2f} {self.moneda}'

    def obtener_nombre_banco(self):
        return self.nombre_banco

    def __str__(self):
        return f'Cuenta: {self.numero_cuenta} - Saldo: {self.obtener_saldo()} - Titular: {self.cliente}'
