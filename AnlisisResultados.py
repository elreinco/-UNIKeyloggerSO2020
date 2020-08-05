# conteo de ocurrencia de letras:
import collections
import pprint
import os

contenido = os.listdir()

for filetxt in contenido:
	if filetxt[-4:] =='.txt':
		with open(filetxt, 'r') as f:
    			conteo_caracteres = collections.Counter(f.read().upper())
    			salida = pprint.pformat(conteo_caracteres)

print(salida)
	