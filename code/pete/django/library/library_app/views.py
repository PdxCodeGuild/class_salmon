from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse

from .models import Book, Author

def index(request):
  authors = Author.objects.all()
  context = {'authors': authors}
  return render(request, 'library_app/index.html', context)

def author_detail(request, id):
  author = get_object_or_404(Author, id=id)
  context = {'author': author}
  return render(request, 'library_app/author.html', context)

def add_author(request):
  name = request.POST['name']
  author = Author.objects.create(name=name)
  return HttpResponseRedirect(reverse('library:author', args=(author.id,)))

def delete_author(request, id):
  author = get_object_or_404(Author, id=id)
  author.delete()
  return HttpResponseRedirect(reverse('library:index'))

def update_author(request, id):
  author = get_object_or_404(Author, id=id)
  author.name = request.POST['name']
  author.save()
  return HttpResponseRedirect(reverse('library:author', args=(author.id,)))

def add_book(request, author_id):
  title = request.POST['title']
  Book.objects.create(author_id=author_id, title=title)
  return HttpResponseRedirect(reverse('library:author', args=(author_id,)))