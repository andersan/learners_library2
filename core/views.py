from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader

from .models import Language, Book

def index(request):
	book_list = Book.objects.order_by('title')
	context = {
		'book_list': book_list,
	}
	return render(request, 'core/index.html', context) # this is the standard way to serve assets/templates - use this format for the other requests once I've created basic views

def search(request, params):
	r = "You searched for %s. Sorry, but our search feature hasn't been built yet."
	return HttpResponse(r % params);

def details(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, 'core/details.html', 
		{'book': book, 
		'url': book.download_set.order_by('rating')[0].url,
		'word_count': book.word_set.count() })

def about(request):
	return HttpResponse("This website is a work in progress - more info later.")

def browse(request):
	book_list = Book.objects.order_by('title')
	context = {
		'book_list': book_list,
	}
	return render(request, 'core/browse.html', context) # this is the standard way to serve assets/templates - use this format for the other requests once I've created basic views
