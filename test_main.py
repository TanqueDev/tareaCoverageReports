import pytest

from main import division, multiplicacion, resta, suma


def test_suma():
  assert suma(2,2) == 4
  assert suma(2,-3) == -1
  
def test_resta():
  assert resta(2,2) == 0
  assert resta(2,-3) == 5
  
def test_multiplicacion():
  assert multiplicacion(2,2) == 4
  assert multiplicacion(2,-6) == -12
  
def test_division():
  assert division(-1,2) == -0.5
  assert division(2,2) == 1
  
def test_division_por_cero():
  with pytest.raises(ZeroDivisionError):
    division(2,0)
