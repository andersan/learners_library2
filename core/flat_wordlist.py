from wordfreq import get_frequency_list	 

#TODO: set up wordlist import
def get_wordlist():
	log_list = get_frequency_list('en')
	index = 1
	subindex = 1
	ordered_dict = {}
	for li in log_list:
		for word in li:
			ordered_dict[word] = index
			subindex += 1
		index = subindex
	return ordered_dict

def ordered_word_frequency(word, word_list):
	try:
		return word_list[word]
	except KeyError:
		return None
