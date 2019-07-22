from django.contrib import admin

from core.models import *
from core.get_gutenberg_data import set_book_stats, get_readability_stats, get_raw_stats
from decimal import Decimal
# Register your models here.

admin.site.register(Language)
# admin.site.register(Book)
admin.site.register(Book_Stats)
admin.site.register(Book_Readability)
admin.site.register(Book_Text)
admin.site.register(Keyword)
admin.site.register(Download)
admin.site.register(Word_Counter)



def save_book_stats(modeladmin, request, book):
	book = book[0]
	if (book.book_text == None or
		len(book.book_text.text) == None or
		len(book.book_text.text) < 10):
		print("No book text imported for book" + book.title + \
			". Please set a book text to get stats about the book.")
		return None
	else:
		set_book_stats(book, 
			stats={
				'readability': get_readability_stats(book.book_text.text),
				'general': get_raw_stats(book, book.book_text.text)
			})
		book.save()

class BooksInstanceInline(admin.TabularInline):
	model = Book_Text

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	date_heirarchy = (
		'modified',
	)
	list_display = (
		'title',
		'author',
	)
	list_select_related = (
		'book_text',
		'book_stats',
		'book_readability',
	)
	inlines = [BooksInstanceInline]
	actions = [save_book_stats]