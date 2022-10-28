from django.shortcuts import render, redirect

from Book_Talk.web.forms.book_forms import BookCreateReviewForm, BookDeleteReviewForm, BookEditReviewForm
from Book_Talk.web.forms.user_forms import UserRegisterForm
from Book_Talk.web.models import User, Book


def homepage(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'GET':
        form = UserRegisterForm()
    else:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {
        'form': form,
        'hide_nav_links': True,
    }
    return render(request, 'register.html', context)


def profile(request):
    user_profile = User.objects.first()
    context = {
        'user_profile': user_profile,
    }
    return render(request, 'profile.html', context)


def catalog(request):
    books = Book.objects.all().order_by('title')
    context = {
        'books': books,
    }
    return render(request, 'catalog.html', context)


def book_details(request, pk):
    book = Book.objects\
        .filter(pk=pk)\
        .get()

    context = {
        'book': book,
    }
    return render(request, 'details.html', context)


def book_add_to_wishlist(request, pk):
    """
        - book_id
        - user_id
    """
    user_profile = User.objects.first()
    book = Book.objects.filter(pk=pk).get()

    user_profile.wishing_list.add(book)
    return redirect('book details', pk=book.pk)


def create_book_review(request):
    user_profile = User.objects.first()

    if request.method == 'GET':
        form = BookCreateReviewForm()
    else:
        book_instance = Book(owner=user_profile)
        form = BookCreateReviewForm(request.POST, request.FILES, instance=book_instance)

        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def book_edit(request, pk):
    book = Book.objects \
        .filter(pk=pk) \
        .get()

    if request.method == 'GET':
        form = BookEditReviewForm(instance=book)
    else:
        form = BookEditReviewForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book details', book.pk)

    context = {
        'form': form,
        'book': book,
    }
    return render(request, 'edit.html', context)


def book_delete(request, pk):
    book = Book.objects\
        .filter(pk=pk)\
        .get()

    if request.method == 'GET':
        form = BookDeleteReviewForm(instance=book)
    else:
        form = BookDeleteReviewForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('catalog')

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'delete.html', context)

