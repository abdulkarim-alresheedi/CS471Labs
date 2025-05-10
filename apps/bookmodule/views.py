from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from django.db.models import Q
from django.db.models import Count, Avg, Max, Min, Sum
from .models import Student, Address, Course, Department, Card
from django.db.models import Count
from django.db.models import Min
from .forms import BookForm
from .models import Student
from .forms import StudentForm
from.forms import GalleryForm
from.models import Gallery
from.forms import Student2Form
from .models import Student2



#from django.http import HttpResponse
from django.shortcuts import render


#def index(request):
    #return HttpResponse("Hello, world!")

from django.http import HttpResponse

#def index(request):
   # name = request.GET.get("name") or "world!"
    #return render("Hello, " + name)
def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
def html5_links(request):
    return render(request, "bookmodule/links.html")
def html5_text_formatting(request):
    return render(request, "bookmodule/text_formatting.html")
def html5_listing(request):
    return render(request, "bookmodule/listing.html")
def html5_tables(request):
    return render(request, "bookmodule/tables.html")



def index2(request, val1=0):  
    return render("value1 = " + str(val1))

from django.shortcuts import render

def viewbook(request, bookId):
    
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    targetBook = None

    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook} 
    return render(request, 'bookmodule/show.html', context)

def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False

            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}

    return [book1, book2, book3]

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')  
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=False)\
        .filter(title__icontains='and')\
        .filter(edition__gte=2)\
        .exclude(price__lte=100)[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    

def task1_view(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})

def task2_view(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})

def task3_view(request):
    books = Book.objects.exclude(
        Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})

def task4_view(request):
    books = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/task4.html', {'books': books})

def task5_view(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

def task7_view(request):
    results = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'results': results})


def task91_view(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task91.html', {'departments': departments})

def task92_view(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task92.html', {'courses': courses})

def task93_view(request):
    departments = Department.objects.all()
    results = []

    for dept in departments:
        student = dept.student_set.order_by('id').first()
        if student:
            results.append({'department': dept.name, 'student': student.name})
    
    return render(request, 'bookmodule/task93.html', {'results': results})

def task94_view(request):
    departments = Department.objects.annotate(student_count=Count('student'))\
        .filter(student_count__gt=2).order_by('-student_count')
    return render(request, 'bookmodule/task94.html', {'departments': departments})


def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        price = request.POST['price']
        edition = request.POST['edition']
        Book.objects.create(title=title, author=author, price=price, edition=edition)
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/addbook.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.price = request.POST['price']
        book.edition = request.POST['edition']
        book.save()
        return redirect('/books/lab9_part1/listbooks')
    return render(request, 'bookmodule/editbook.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/books/lab9_part1/listbooks')




def list_books_form(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/part2_listbooks.html', {'books': books})

def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books_form')
    else:
        form = BookForm()
    return render(request, 'bookmodule/part2_addbook.html', {'form': form})

def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('list_books_form')
    return render(request, 'bookmodule/part2_editbook.html', {'form': form})

def delete_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('list_books_form')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})


def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})


def student_edit(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'student/student_form.html', {'form': form})

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')

def upload_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = GalleryForm()
    return render(request, 'gallery/image_form.html', {'form': form})


def student2_list(request):
    students = Student2.objects.all()
    return render(request, 'student2/student2_list.html', {'students': students})

def student2_add(request):
    form = Student2Form(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student2_list')
    return render(request, 'student2/student2_form.html', {'form': form})

def student2_edit(request, id):
    student = get_object_or_404(Student2, id=id)
    form = Student2Form(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student2_list')
    return render(request, 'student2/student2_form.html', {'form': form})

def student2_delete(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('student2_list')




def upload_image(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('image_list')
    else:
        form = GalleryForm()
    return render(request, 'gallery/image_form.html', {'form': form})

def image_list(request):
    images = Gallery.objects.all()
    return render(request, 'gallery/image_list.html', {'images': images})