from alive_progress import alive_bar
from time import sleep

with alive_bar(100) as bar:		#Configuración por default
	for i in range(100):
		sleep(0.03)
		bar()			#Actualiza la barra despues de cada ejecución

with alive_bar(200, bar='checks', spinner='notes2') as bar:	#usando palomitas en la barra y notas en el spinner
	for i in range(200):
		sleep(0.03)
		bar()