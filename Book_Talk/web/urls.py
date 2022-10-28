from django.urls import path

from Book_Talk.web.views import homepage, catalog, register, profile, \
    create_book_review, book_details, book_delete, \
    book_edit, book_add_to_wishlist

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),

    path('catalog/', catalog, name='catalog'),
    path('book/<int:pk>/', book_details, name='book details'),
    path('book/delete/<int:pk>/', book_delete, name='book delete'),
    path('book/<int:pk>/add-to-wishlist/', book_add_to_wishlist, name='book add to wishlist'),
    path('book/edit/<int:pk>/', book_edit, name='book edit'),
    path('create/', create_book_review, name='create book review'),
]
