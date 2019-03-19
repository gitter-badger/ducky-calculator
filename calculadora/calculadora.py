import sys

import inspect

import funciones as fn


def main():
    funciones = (
        fn.suma,
        fn.resta,
        fn.raices,
        fn.integral_definida,
    )
    print('Ducky v1.0')
    while(True):
        print('0.- salir: Termina el programa')
        for idx, funcion in enumerate(funciones, start=1):
            print('{indice}.- {nombre}: {descripcion}'.format(
                indice=idx,
                nombre=funcion.__name__,
                descripcion=funcion.__doc__.split('\n')[0]
            ))
        choice = int(input("Elgie una función a utilizar: "))
        if choice == 0:
            break
        funcion = funciones[choice-1]
        firma = inspect.signature(funcion)
        argumentos = []
        for parametro in firma.parameters:
            arg = input('Ingresa el valor de {}: '.format(parametro))
            try:
                arg = int(arg)
            except ValueError:
                pass
            argumentos.append(arg)
        resultado = funcion(*argumentos)
        print("El resultado fue: {}".format(resultado))
        print()
    print("Gracias por utilizar Ducky")


if __name__ == '__main__':
    sys.exit(main())
