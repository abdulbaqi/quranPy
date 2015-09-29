import codecs

def ReadQuran(file='quran-simple-clean.txt'):
	f = codecs.open(file, encoding='utf-8', mode='r')
	quran = []
	for line in f:
	    vid = line.split('|')[0]+':'+line.split('|')[1]
	    v = line.split('|')[2]
	    quran.append({'vid':vid, 'v':v})
	return quran


