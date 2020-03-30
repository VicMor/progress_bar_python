from time import sleep
from progressbar import progressbar


for i in progressbar(range(50), redirect_stdout=True):
	print('Algo de texto',i)
	sleep(0.02)