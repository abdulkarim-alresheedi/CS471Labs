from django.urls import path
from . import views 
urlpatterns = [ 
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.html5_links, name="books.links"),
    path('html5/text/formatting/', views.html5_text_formatting, name="books.text_formatting"),
    path('html5/listing/', views.html5_listing, name="books.listing"),
    path('html5/tables/', views.html5_tables, name="books.tables"),
    path('search/', views.search_books, name='search_books'),
    path('books/simple/query', views.simple_query, name='simple_query'),
    path('books/complex/query', views.complex_query, name='complex_query'),
    path('books/lab8/task1', views.task1_view),
    path('books/lab8/task2', views.task2_view),
    path('books/lab8/task3', views.task3_view),
    path('books/lab8/task4', views.task4_view),
    path('books/lab8/task5', views.task5_view),
    path('books/lab8/task7', views.task7_view),
    path('books/lab9/task1', views.task91_view),
    path('books/lab9/task2', views.task92_view),
    path('books/lab9/task3', views.task93_view),
    path('books/lab9/task4', views.task94_view),










 ] 