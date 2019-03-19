import sympy as sp
sp.init_printing(use_unicode=True)


def suma(a, b):
    """Suma dos números

    Args:
        a (Numero): Numero a la izquierda del operador
        b (Numero): Numero a la derecha del operador

    Returns:
        Numero: El resultado de la suma
    """

    return a + b


def resta(a, b):
    """Suma dos números

    Args:
        a (Numero): Numero a la izquierda del operador
        b (Numero): Numero a la derecha del operador

    Returns:
        Numero: El resultado de la suma
    """

    return a - b


def raices(funcion):
    """Calcula la raíz de la función en base a x

    Args:
        funcion (String): La funcion, que debe incluir el símbolo 'x'

    Returns:
        List[Expr]: Las raices de la función
    """
    return sp.solve(funcion, 'x')


def integral_definida(funcion, a, b):
    """Regresa el area bajo la curva de la funcion desde a hasta b
    
    Args:
        funcion (String): La funcion a integrar
        a (Numero): Limite inferior
        b (Numero): Limite superior
    
    Returns:
        result: El area bajo la curva
    """

    result = sp.integrate(funcion, ('x', a, b))
    return result