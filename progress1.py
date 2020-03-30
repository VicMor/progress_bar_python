from time import sleep
from progress.bar import Bar


with Bar('Procesando...', fill='@', suffix='%(percent).1f%% - %(eta)ds', ) as bar:
	for i in range(100):
		sleep(0.02)
		bar.next()			#Sirve para actualizar la barra de progreso