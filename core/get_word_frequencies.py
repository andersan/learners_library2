from core.count_book_tokens import count_book_tokens
from core.flat_wordlist import get_wordlist, ordered_word_frequency
import ujson

# Counts and saves book tokens if necessary. Returns the average index on 
# 	an ordered wordlist for the book's words.
def get_average_frequency(book, total_words):
	if book.book_text: # unsure if this works... use == None?
		count_book_tokens(book) # goal: Count the book's tokens
	else: 
		return # throw error?
	top = 0
	word_list = get_wordlist()
	word_count_dict = ujson.loads(book.word_counter.counter)
	for word in word_count_dict:
		this_word_frequency = ordered_word_frequency(word, word_list)
		if this_word_frequency:
			top += word_count_dict[word] * this_word_frequency
	average = top / total_words
	return average
