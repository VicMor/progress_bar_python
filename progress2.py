from time import sleep
from progress.spinner import MoonSpinner


with MoonSpinner('Procesando ...') as bar:
	for i in range(100):
		sleep(0.04)
		bar.next()