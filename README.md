# tareaCoverageReports en Python
<p align="justify">
Antes de iniciar con la explicación acerca de lo que se realizó por medio de la tarea, es importante mencionar que las commits se hicieron a través de la página Replit.com. Esto es importante puesto que la página nos habilita una pequeña máquina virtual en la que se ejecuta el código que estamos escribiendo, por lo que al momento de trabajar,en el directorio principal se crean otros archivos y carpetas adicionales en los que se guardan la configuración de librerías y parámetros adicionales que son necesarios para el funcionamiento del código.
Esa es la razón por la cual hay archivos demás en el directorio. Esta decisión la tomé debido a que la librería de pytest no funcionó correctamente en mí PC, por lo que debo desinstalar Linux e instalarlo de nuevo.

Dicho esto, empecemos explicando parte por parte los códigos que se encuentran tando en main.py como en test_main.py
</p>

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
<p align="justify">
En el código, como fue pedido originalmente se definieron funciones que realizan las cuatro operaciones básicas: Suma, resta, multiplicación y división.
Es importante mencionar que en la función de división, se definió una excepción para los casos en los que B sea cero, que es una excepción ZeroDivisionError. Esto es con el objetivo de identificar en qué pruebas se introdujo un cero como divisor y así cuando al ejecutar el código con un parámetro igual a cero para el denominador, se lance una excepción de división entre 0.
</p>

## Explicación de test_main.py


>Antes de iniciar, es importante remarcar que el nombre del archivo debe de tener como nombre test_(nombre del archivo principal).py debido a que si no se marca con el sufijo test_ al inicio la librería pytest no lo reconocerá para hacer las pruebas. Lo mismo se cumple con cualquier función de prueba que se vaya a programar en este archivo. 
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
<p align="justify">
En este código se definen distintas funciones que permiten hacer test concernientes a las funciones suma, resta, multiplicación y división del archivo main.py 
Para esto se utiliza la librería pytest, que mediante el comando assert nos permite establecer si el valor retornado por una función es efectivamente el esperado dado el comportamiento programado por el desarrollador.
</p>
## Informe de cobertura, coverage HTML (Carpeta htmlcov).

[![image.png](https://i.postimg.cc/hGPrSSS1/image.png)](https://postimg.cc/ZW23HzvW)

<p align="justify">
El reporte de cobertura, dado por la librería Coverage de Python, nos permite saber qué porcentaje del código se está sometiendo a pruebas correctamente dado un conjunto de funcionalidades y archivo de código programados, y su respectivo archivo de pruebas.

Para ejecutar el informe de cobertura, se empieza por llamar a la consola, bash o shell de nuestro entorno de desarrollo y se llama al comando:
</p>

```bash
 coverage run -m pytest
```
Que lo que hace es poner a correr las pruebas programadas por medio de la librería pytest, para poder luego revisar cuáles líneas de código se están probando correctamente con las pruebas que se programaron.

Después de esto, utilizamos los comandos:

```bash
coverage report
coverage html
```
<p align="justify">
Para generar un reporte en HTML de la cobertura del código. En este caso, el reporte generado fue el que se mostró en la imagen anterior. Como es posible apreciar, este archivo de cobertura cuenta en la parte superior con una serie de botones que nos permiten revisar cuáles son las funciones y clases que están definidas en el código, además de directamente un botón que nos muestra información general acerca de los archivos testeados, en este caso el archivo main.py y el archivo test_main.py
</p>

[![image.png](https://i.postimg.cc/vHJkHxjL/image.png)](https://postimg.cc/LnVNx5mn)

<p align="justify">
Como anteriormente se mostró en la imagen inicial, hay una cobertura de 100% del código, aunque analicemoslo desde la opción de funciones del reporte de cobertura para tener un poco más de detalle acerca de qué fue lo que realizó esta librería. 
</p>

[![image.png](https://i.postimg.cc/3xQfH54t/image.png)](https://postimg.cc/JGK5bFQX)

<p align="justify">
Lo que es posible apreciar de esta imagen son 6 distintos encabezados en una tabla que encapsulan a todas y cada una de las funciones del código que se probó por medio de pytest. A la izquierda del todo encontramos el archivo al que pertenece cada función, y en las siguientes casillas se encuentran tanto el nombre de la función como el número de lineas que tiene (statements) las líneas que no se probaron (missing) o que fueron excluidas de la prueba (excluded) y por último el porcentaje de coverage o cobertura de las pruebas programadas. En este caso, el porcentaje de coverage fue de un 100% puesto que las pruebas diseñadas probaron todas y cada una de las líneas de código del archivo principal main.py satisfactoriamente.
</p>
