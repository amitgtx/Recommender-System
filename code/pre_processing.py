from sets import Set
from stop_words import get_stop_words
from nltk import PorterStemmer
from nltk import pos_tag,word_tokenize
import os

script_path = os.path.abspath(__file__)
script_dir = os.path.split(script_path)[0]
stop = set(get_stop_words('en'))

for i in range(1,11):

		print "[file",i,"]"
		filename=script_dir+"/input_data/d"+str(i)
		target=script_dir+"/output_data/f"+str(i)
		txt = open(filename)
		out=open(target,'w')
		out.truncate()

		# Removing stopwords
		print "Removing stopwords ..."
		f= txt.read().split()
		nf=[]
		for i in f:
			if(i not in stop):nf.append(i)


		# # Tagging each word and extracting nouns
		print "Tagging each word and extracting nouns.."
		tagged = pos_tag(nf)
		nouns=[x for x,y in tagged if y.startswith("NN")]
		nouns=set(nouns)


		# # Stemming each word
		print "Stemming each word"
		new_str=""
		for i in nouns:
			new_str+= PorterStemmer().stem_word(i)+" "

		out.write(new_str+"\n")






