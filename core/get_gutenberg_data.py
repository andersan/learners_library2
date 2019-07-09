import textstat
import time
from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from core.models import Book, Book_Readability, Book_Stats
from core.get_word_frequencies import get_average_frequency
from decimal import getcontext, Decimal, DecimalException
from nltk import sent_tokenize
from nltk import download

top_books = [2701, #moby dick
1342, #jane austen
1661, #sherlock holmes
]

def ts_gb_test():
	get_stats(load_etext(2701))
	get_stats(load_etext(1342))
	get_stats(load_etext(1661))

def get_gutenberg_book(book):
	text = load_etext(book.gutenberg_id)
	return text

#alculate readability stats, save stats
def get_readability_stats(text):
	return {
		'flesch_reading_ease': textstat.flesch_reading_ease(text),
		'smog_index': textstat.smog_index(text),
		'flesch_kincaid_grade': textstat.flesch_kincaid_grade(text),
		'coleman_liau_index': textstat.coleman_liau_index(text),
		'automated_readability_index': textstat.automated_readability_index(text),
		'dale_chall_readability_score': textstat.dale_chall_readability_score(text),
		'linsear_write_formula': textstat.linsear_write_formula(text),
		'gunning_fog': textstat.gunning_fog(text),
		'text_standard': textstat.text_standard(text, float_output=True),
	}

def get_raw_stats(book, text):
	download('punkt')
	return {
		'total_words': textstat.lexicon_count(text),
		'total_sentences': len(sent_tokenize(text)),
		'total_letters': textstat.letter_count(text),
		'total_syllables': textstat.syllable_count(text),
		# 'total_paragraphs': len(get_paragraphs(text)),
		# 'average_word_difficulty': get_average_frequency(book)
	}

def set_book_stats(book, stats):
	getcontext().prec = 2 # sets max decimal places to 2
	if book.has_book_readability():
		book.book_readability.delete()
	br = Book_Readability(
		book = book,
		textstat_rating = Decimal(stats['readability']['text_standard']),
		flesch_reading_ease = Decimal(stats['readability']['flesch_reading_ease']),
		smog_index = Decimal(stats['readability']['smog_index']),
		flesch_kincaid_grade = Decimal(stats['readability']['flesch_kincaid_grade']),
		coleman_liau_index = Decimal(stats['readability']['coleman_liau_index']),
		automated_readability_index = Decimal(stats['readability']['automated_readability_index']),
		dale_chall_readability_score = Decimal(stats['readability']['dale_chall_readability_score']),
		linsear_write_formula = Decimal(stats['readability']['linsear_write_formula']),
		gunning_fog = Decimal(stats['readability']['gunning_fog'])
	)
	br.save()
	if book.has_book_stats():
		book.book_stats.delete()
	bs = Book_Stats(
		book = book,
		total_words = stats['general']['total_words'],
		total_sentences = stats['general']['total_sentences'],
		total_letters = stats['general']['total_letters'],
		# total_paragraphs = stats['general']['total_paragraphs'],
		total_syllables = stats['general']['total_syllables'],
		average_word_difficulty = get_average_frequency(book, stats['general']['total_words'])
	) # put relevant stats here
	bs.save()
	link = "http://www.gutenberg.org/ebooks/" + str(book.gutenberg_id) 
	download = book.download_set.create(url=link, clicks=0, rating=0)
	download.save()

# def get_word_difficulty(book):
# 	difficulty = 0
# 	book.book_text
# 	# get difficulty of all words (add up frequency in word list)
# 	# save this data (which words, their frequency)
# 	# calculate average word difficulty
# 	return difficulty