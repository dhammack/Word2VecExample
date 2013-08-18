import pickle
import numpy as np

def main():
	cutoff = 20000
	with open('vectors.txt', 'r') as f:
		i = 0
		ind = 0
		lines = []
		for line in f:
			lines.append(line)
			i+= 1
			if i > cutoff:
				i = 0
				with open('vectors'+str(ind)+'.txt', 'w') as fout:
					for readline in lines:
						fout.write(readline)
				ind += 1
				lines = []
		
		with open('vectors'+str(ind)+'.txt', 'w') as fout:
					for readline in lines:
						fout.write(readline)
	
if __name__ == '__main__':
	main()
	