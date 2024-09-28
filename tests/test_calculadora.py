import pytest
from src.calculadora import Calculadora

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (0,0,0),
    (-1,-1,-2)
])
def test_somar_deve_retornarsomavalida(a,b,expected):
    #Arrange
    calc = Calculadora()
    #Act
    actual = calc.somar(a,b)
    #Assert
    assert actual == expected


@pytest.mark.parametrize("a,b,expected", [
    (2,1,1),
    (0,0,0),
    (-1,-1,0)
])
def test_subtrair_deve_retornarresultadovalida(a,b,expected):
    #Arrange
    calc = Calculadora()
    #Act
    actual = calc.subtrair(a,b)
    #Assert
    assert actual == expected

@pytest.mark.parametrize("a,b,expected", [
    (2,3,6),
    (0,0,0),
    (-1,-1,1)
])
def test_multiplicar_deve_retornarprodutovalido(a,b,expected):
    #Arrange
    calc = Calculadora()
    #Act
    actual = calc.multiplicar(a,b)
    #Assert
    assert actual == expected