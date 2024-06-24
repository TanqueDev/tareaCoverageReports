# tareaCoverageReports
Antes de iniciar con la explicación acerca de lo que se realizó por medio de la tarea, es importante mencionar que las commits se hicieron a través de la página Replit.com. Esto es importante puesto que la página nos habilita una pequeña máquina virtual en la que se ejecuta el código que estamos escribiendo, por lo que al momento de trabajar,en el directorio principal se crean otros archivos y carpetas adicionales en los que se guardan la configuración de librerías y parámetros adicionales que son necesarios para el funcionamiento del código.
Esa es la razón por la cual hay archivos demás en el directorio. Esta decisión la tomé debido a que la librería de pytest no funcionó correctamente en mí PC, por lo que debo desinstalar Linux e instalarlo de nuevo.

Dicho esto, empecemos explicando parte por parte los códigos que se encuentran tando en main.py como en test_main.py

## Explicación de main.py
Código de main.py:
```python
def suma(a,b):
  return a+b
def resta(a,b):
  return a-b
def multiplicacion(a,b):
  return a*b
def division(a,b):
  if b==0:
    raise ZeroDivisionError("No se puede dividir entre 0")
  return a/b
```
En el código, como fue pedido originalmente se definieron funciones que realizan las cuatro operaciones básicas: Suma, resta, multiplicación y división.
Es importante mencionar que en la función de división, se definió una excepción para los casos en los que B sea cero, que es una excepción ZeroDivisionError. Esto es con el objetivo de identificar en qué pruebas se introdujo un cero como divisor y así cuando al ejecutar el código con un parámetro igual a cero para el denominador, se lance una excepción de división entre 0.

## Explicación de test_main.py
Código de test_main.py:
```python
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
```
