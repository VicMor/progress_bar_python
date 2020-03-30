from time import sleep
from progress.bar import Bar


#Combining progress-bar with print output
with Bar('Procesando ...', max=5) as bar:
	for i in range(5):
		sleep(0.02)
		print('\n',i)
		bar.next()