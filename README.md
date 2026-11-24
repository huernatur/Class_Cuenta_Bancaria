# Banco de la UAX

Programa sencillo en Python que simula algunas operaciones de un banco. Es un ejercicio de programación orientada a objetos de Fundamentos de Informática del Grado en Ciencias Físicas.

## Funcionamiento

El programa permite crear clientes, abrir cuentas bancarias, ingresar y retirar dinero, consultar los saldos y salir. Un cliente puede tener varias cuentas. El PIN es opcional y, si se introduce, se pide al ingresar o retirar dinero.

## Archivos

- `classes.py`: contiene las clases Cliente y CuentaBancaria.
- `script.py`: contiene el menú y las operaciones del programa.
- `.gitignore`: indica qué archivos no debe guardar Git.
- `.gitattributes`: configura el tratamiento de los archivos de texto en Git.

## Cómo ejecutar el programa

Se necesita Python 3. No es necesario instalar ninguna librería adicional. Desde la terminal, dentro de la carpeta del proyecto, ejecutar:

```bash
python script.py
```

En algunos equipos se utiliza `python3 script.py` o `py script.py`.

## Ejemplo

Primero se crea un cliente y después una cuenta a su nombre. Si se ingresan 100 euros y se retiran 30 euros, el saldo final es de 70 euros. El programa no permite retirar más dinero del disponible.

## Conceptos utilizados

Clases, objetos, atributos, métodos, listas, funciones, bucles, condicionales y control básico de errores con try y except.

Los datos se guardan en listas mientras el programa está abierto. Al cerrarlo se pierden. Es una simulación educativa, no un sistema bancario real; no se deben introducir datos personales ni PIN reales.
