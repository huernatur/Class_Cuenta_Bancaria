from classes import Cliente, CuentaBancaria


def seleccionar(lista):
    # Mostramos los elementos numerados para poder elegir uno.
    if len(lista) == 0:
        print('No hay elementos registrados.')
        return None

    for i in range(len(lista)):
        print(f'{i + 1}. {lista[i]}')

    try:
        numero = int(input('Seleccione un número: '))
        if 1 <= numero <= len(lista):
            return lista[numero - 1]
    except ValueError:
        pass

    print('Selección incorrecta.')
    return None


def main():
    clientes = []
    cuentas = []
    activo = True

    while activo:
        print('\nBienvenido al banco de la UAX')
        print('1. Crear cliente')
        print('2. Crear cuenta bancaria')
        print('3. Ingresar dinero')
        print('4. Retirar dinero')
        print('5. Consultar cuentas y saldos')
        print('6. Salir')
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            nombre = input('Nombre: ').strip()
            apellido = input('Apellido: ').strip()
            if nombre == '' or apellido == '':
                print('Debe introducir un nombre y un apellido.')
            else:
                pin = input('PIN opcional (4 cifras): ').strip()
                if pin != '' and (len(pin) != 4 or not pin.isdigit()):
                    print('El PIN debe tener cuatro cifras.')
                else:
                    cliente = Cliente(nombre, apellido, pin or None)
                    clientes.append(cliente)
                    print(f'Cliente creado: {cliente}')

        elif opcion == '2':
            cliente = seleccionar(clientes)
            if cliente is not None:
                # Cada cuenta tiene un número distinto.
                numero = len(cuentas) + 1
                cuenta = CuentaBancaria(numero, cliente)
                cuentas.append(cuenta)
                print(f'Cuenta creada: {cuenta}')

        elif opcion == '3' or opcion == '4':
            cuenta = seleccionar(cuentas)
            if cuenta is not None:
                if cuenta.cliente.pin is not None:
                    pin = input('Introduzca el PIN: ')
                    if pin != cuenta.cliente.pin:
                        print('PIN incorrecto.')
                        continue
                try:
                    cantidad = round(float(input('Cantidad en euros: ').replace(',', '.')), 2)
                except (ValueError, OverflowError):
                    print('Introduzca una cantidad válida.')
                    continue

                if opcion == '3':
                    correcto = cuenta.ingresar(cantidad)
                else:
                    correcto = cuenta.retirar(cantidad)

                if correcto:
                    print(f'Operación realizada. Saldo: {cuenta.obtener_saldo()}')
                else:
                    print('Cantidad no válida o saldo insuficiente.')

        elif opcion == '5':
            if len(cuentas) == 0:
                print('No hay cuentas registradas.')
            else:
                for cuenta in cuentas:
                    print(cuenta)

        elif opcion == '6':
            activo = False
            print('Gracias por usar el banco de la UAX. ¡Hasta luego!')
        else:
            print('Opción incorrecta.')


if __name__ == '__main__':
    main()
