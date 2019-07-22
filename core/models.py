import uuid

from django.db import models

# Create your models here.

class Language(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=31)
	short_code = models.CharField(max_length=8)
	def __str__(self):
		return self.name

class Keyword(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	word = models.CharField(max_length=63)
	def __str__(self):
		return self.word

# class BookManager(models.Manager):
# 	def create_book(self, title, text):
# 		book = self.create(title=title)
# 		book.book_text.create()
# 		self.set_book_text(book, text)
# 	def set_book_text(book, text):
# 		book.book_text.text = text
# 	def save_book_stats(modeladmin, request, book):
# 		if (book.book_text == None or
# 			len(book.book_text.text) == None or
# 			len(book.book_text.text) < 10):
# 			print("No book text imported for book" + book.title + \
# 				". Please set a book text to get stats about the book.")
# 			return None
# 		else:
# 			set_book_stats(book, 
# 				stats={
# 					'readability': get_readability_stats(book.book_text),
# 					'general': get_raw_stats(book, book.book_text)
# 				})
# 			book.save()

class Book(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=255)
	description = models.TextField(blank=True, null=True)
	author = models.CharField(max_length=63)
	isbn = models.CharField(max_length=31, blank=True, null=True) #number, max 13 digits
	publication_date = models.DateField(blank=True, null=True)
	publisher = models.CharField(max_length=31, blank=True, null=True)
	publication_location = models.CharField(max_length=31, blank=True, null=True)
	version = models.CharField(max_length=31, blank=True, null=True)
	language = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
	gutenberg_id = models.PositiveIntegerField(blank=True, null=True)
	cover_image = models.ImageField(upload_to='book_images', blank=True, null=True)
	keywords = models.ManyToManyField(Keyword)
	# objects = BookManager()
	def __str__(self):
		return self.title
	def has_word_counter(self):
	    has_word_counter = False
	    try:
	        has_word_counter = (self.word_counter is not None)
	    except Word_Counter.DoesNotExist:
	        pass
	    return has_word_counter
		# return hasattr(self, 'word_counter') and self.book is not None
	def has_book_stats(self):
	    has_book_stats = False
	    try:
	        has_book_stats = (self.book_stats is not None)
	    except Book_Stats.DoesNotExist:
	        pass
	    return has_book_stats
	def has_book_readability(self):
	    has_book_readability = False
	    try:
	        has_book_readability = (self.book_readability is not None)
	    except Book_Readability.DoesNotExist:
	        pass
	    return has_book_readability

class Book_Readability(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
	book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_readability')
	textstat_rating = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
	flesch_reading_ease = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	smog_index = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	flesch_kincaid_grade = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	coleman_liau_index = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	automated_readability_index = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	dale_chall_readability_score = models.DecimalField(decimal_places=2,max_digits=5, blank=True, null=True)
	linsear_write_formula = models.DecimalField(decimal_places=2,max_digits=5,blank=True, null=True)
	gunning_fog = models.DecimalField(decimal_places=2,max_digits=5,blank=True, null=True)
	def __str__(self):
		return self.book.title

class Word_Counter(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='word_counter')
	counter = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.book.title

class Book_Stats(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_stats')
	total_words = models.PositiveIntegerField(blank=True, null=True)
	total_sentences = models.PositiveIntegerField(blank=True, null=True)
	total_letters = models.PositiveIntegerField(blank=True, null=True)
	total_paragraphs = models.PositiveIntegerField(blank=True, null=True)
	total_syllables = models.PositiveIntegerField(blank=True, null=True)
	average_word_difficulty = models.PositiveSmallIntegerField(blank=True, null=True) ## Will probably add more fields to this model
	def __str__(self):
		return self.book.title

class Book_Text(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='book_text')
	text = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.book.title


class Download(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	url = models.URLField()
	clicks = models.PositiveIntegerField(default=0) 
	rating = models.SmallIntegerField(null=True,default=None)
	def __str__(self):
		return self.book.title
