# Para importar libreria math
import math
# Se puede renombrar la libreria, la llamaremos "mt"
import math as mt
# Ejemplo de uso
# sqrt se usa para calcular raiz cuadrada
print(mt.sqrt(81))
# Si nos dirigimos a la documentación de python figuran las librerías disponibles

# Para utilizar librerías de otro distribuidor, se utiliza ejemplo "pip"
# pip --help para ver los comandos
# Los más utilizados serán "instal", "uninstall", "list", "show"
# Pypi.org para buscar librerías
# Importamos librería colorama
import colorama
print(colorama.Fore.RED + "Some text")
print(colorama.Style.RESET_ALL)
print("Some text")
# También se puede usar comandos en específico sin necesidad de importar la librería completa
# Hace que no sea necesario especificar la librería constantemente
from colorama import Fore, Back, Style
print(Fore.RED + "Some text")
print(Style.RESET_ALL)
print("Some text")
