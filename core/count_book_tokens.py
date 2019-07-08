from nltk.tokenize import word_tokenize
from django.core.exceptions import ObjectDoesNotExist
from core.flat_wordlist import get_wordlist, ordered_word_frequency


def count_book_tokens(book, recount=False):
	if book.word_set.count() > 0 and recount == False:
		return # avoid recounting words 
	book_text = book.book_text.text
	book_tokens = word_tokenize(book_text)
	wordlist = get_wordlist()
	for token in book_tokens:
		if not ordered_word_frequency(token, wordlist):
			continue # skip this token if it isn't a word. 
			# word_tokenize should turn contractions into words.
		try:
			token = token.lower()
			word = book.word_set.get(word=token)
			word.count += 1
		except ObjectDoesNotExist:
			word = None
		if word == None:
			word = book.word_set.create(word=token, count=1)
		word.save()

