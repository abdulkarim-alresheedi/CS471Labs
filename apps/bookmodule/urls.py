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
    path('books/lab9_part1/listbooks', views.list_books),
    path('books/lab9_part1/addbook', views.add_book, name='add_book'),
    path('books/lab9_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
    path('books/lab9_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
    path('lab9_part2/listbooks', views.list_books_form, name='list_books_form'),
    path('lab9_part2/addbook', views.add_book_form, name='add_book_form'),
    path('lab9_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
    path('lab9_part2/deletebook/<int:id>', views.delete_book_form, name='delete_book_form'),
    path('student/', views.student_list, name='student_list'),
    path('student/add/', views.student_add, name='student_add'),
    path('student/edit/<int:id>/', views.student_edit, name='student_edit'),
    path('student/delete/<int:id>/', views.student_delete, name='student_delete'),
    path('student2/', views.student2_list, name='student2_list'),
    path('student2/add/', views.student2_add, name='student2_add'),
    path('student2/edit/<int:id>/', views.student2_edit, name='student2_edit'),
    path('student2/delete/<int:id>/', views.student2_delete, name='student2_delete'),
    path('gallery/upload/', views.upload_image, name='upload_image'),
    path('gallery/list/', views.image_list, name='image_list'),
















 ] 