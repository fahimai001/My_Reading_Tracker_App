from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, UpdateStatusForm

def home(request):
    reading_count = Book.objects.filter(status='reading').count()
    completed_count = Book.objects.filter(status='completed').count()
    total_books = Book.objects.count()
    tech_count = Book.objects.filter(book_type='TECH').count()
    novel_count = Book.objects.filter(book_type='NOVEL').count()
    return render(request, 'home.html', {
        'reading_count': reading_count,
        'completed_count': completed_count,
        'total_books': total_books,
        'tech_count': tech_count,
        'novel_count': novel_count,
    })

def tech_books(request):
    books = Book.objects.filter(book_type='TECH')
    return render(request, 'tech_books.html', {'books': books})

def novel_books(request):
    books = Book.objects.filter(book_type='NOVEL')
    return render(request, 'novel_books.html', {'books': books})

def show_books(request):
    status = request.GET.get('status', 'all')
    if status in ['reading', 'completed', 'not-started']:
        books = Book.objects.filter(status=status)
    else:
        books = Book.objects.all()

    # Optional: provide counts for the filter summary
    reading_count = Book.objects.filter(status='reading').count()
    completed_count = Book.objects.filter(status='completed').count()
    not_started_count = Book.objects.filter(status='not-started').count()

    return render(request, 'show_books.html', {
        'books': books,
        'filter_status': status,
        'reading_count': reading_count,
        'completed_count': completed_count,
        'not_started_count': not_started_count,
    })

def add_tech_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.book_type = 'TECH'  # force Tech Book
            book.save()
            return redirect('tech_books')
    else:
        form = BookForm(initial={'book_type': 'TECH'})
    return render(request, 'add_book.html', {'form': form, 'book_type': 'Tech Book'})

def add_novel_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.book_type = 'NOVEL'  # force Noval Book
            book.save()
            return redirect('novel_books')
    else:
        form = BookForm(initial={'book_type': 'NOVEL'})
    return render(request, 'add_book.html', {'form': form, 'book_type': 'Novel Book'})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = UpdateStatusForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            # Redirect back to the appropriate page based on book type.
            if book.book_type == 'TECH':
                return redirect('tech_books')
            elif book.book_type == 'NOVEL':
                return redirect('novel_books')
            else:
                return redirect('show_books')
    else:
        form = UpdateStatusForm(instance=book)
    return render(request, 'edit_book.html', {'form': form, 'book': book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'confirm_delete.html', {'book': book})
