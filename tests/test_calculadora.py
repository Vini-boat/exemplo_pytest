import pytest
from src.calculadora import somar, subtrair

@pytest.mark.parametrize("a,b,expected", [
    (1,2,3),
    (0,0,0),
    (-1,-1,-2)
])
def test_somar_deve_retornarsomavalida(a,b,expected):
    #Arrange
    #Act
    #Assert
    assert somar(a,b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2,1,1),
    (0,0,0),
    (-1,-1,0)
])
def test_subtrair_deve_retornarresultadovalida(a,b,expected):
    assert subtrair(a,b) == expected