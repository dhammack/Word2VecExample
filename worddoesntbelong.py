#figure out which word of a list doesn't belong!
#use word2vec for vectorization
#compute the mean of the vectors, find the one which is furthest!
import numpy as np
import os

def load_word2vec(dir):
	#new: since github has a 100M limit, load from a bunch of files in 
	#a directory
	word2vec = {}
	for path in os.listdir(dir):
		iword2vec = {}
		#load the word2vec features.
		with open(os.path.join(dir,path), 'r') as fin:
			next(fin) #skip information on first line
			for line in fin:
				items = line.replace('\r','').replace('\n','').split(' ')
				if len(items) < 10: continue
				word = items[0]
				vect = np.array([float(i) for i in items[1:] if len(i) > 1])
				iword2vec[word] = vect
		
		word2vec.update(iword2vec)
		
	return word2vec
    
def get_furthest_word(words, word2vect):
	vectlist = []
	for word in words:
		#unknown word? 
		if word not in word2vect: return word
		vectlist.append(word2vect[word])
	mean = np.array(vectlist).mean(axis=0)

	#figure out which is furthest
	dists = [np.linalg.norm(v - mean) for v in vectlist]
	return words[np.argmax(dists)]

def main():
	print "Hello human. I attempt to find a word in a list which doesn't belong.\n\n"
	print 'loading knowledge from Wikipedia...should take 10-20 seconds'
	word2vec = load_word2vec('vectors')
	print 'Type several words separated by spaces. The more words you enter, the better I can guess.'
	while (True):
		words = raw_input('->').lower().split(' ')
		print 'I think',get_furthest_word(words, word2vec),'doesnt belong in this list!\n'
		
		
if __name__ == '__main__':
    main()