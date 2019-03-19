import pytest
from calculadora import funciones as fn


def test_suma_enteros():
    actual = fn.suma(1, 2)
    expected = 3
    assert actual == expected


def test_resta_enteros():
    assert fn.resta(5, 3) == 2


@pytest.mark.xfail
def test_suma_flotantes():
    assert fn.suma(1.04, 2.10) == 3.14


@pytest.mark.xfail
def test_resta_flotantes():
    assert fn.resta(10.5, 0.5) == 10.0


def test_integral_definida_polinomial():
    assert fn.integral_definida("x**2", 0, 2) == 8/3