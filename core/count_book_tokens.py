from nltk.tokenize import word_tokenize
from django.core.exceptions import ObjectDoesNotExist
from core.flat_wordlist import get_wordlist, ordered_word_frequency
from core.models import Book, Word_Counter
import ujson


## TODO: 	Fix this method / the organization of the Word data in the DB. 
## 			Seems to be Far too expensive to save a new object for each unique word for each book.
##			Not reliable when run on Heroku - use these limitations to rethink this data structure.
##			Another option would be generating all data outside Heroku and importing it there.

def count_book_tokens(book, recount=False):
	try :
		if book.word_counter and recount == False:
			return # avoid recounting words
	except Word_Counter.DoesNotExist:
		pass
	book_text = book.book_text.text
	book_tokens = word_tokenize(book_text)
	wordlist = get_wordlist()
	word_count_dict = {}
	for token in book_tokens:
		if not ordered_word_frequency(token, wordlist):
			continue # skip this token if it isn't a word. 
			# word_tokenize should turn contractions into words.
		token = token.lower()
		if token in word_count_dict:
			word_count_dict[token] += 1
		else:
			word_count_dict[token] = 1
	counter = Word_Counter(
		book = book,
		counter = ujson.dumps(word_count_dict)
		)
	counter.save()