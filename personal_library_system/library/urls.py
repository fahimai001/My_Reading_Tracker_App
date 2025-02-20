from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tech/', views.tech_books, name='tech_books'),
    path('tech/add/', views.add_tech_book, name='add_tech_book'),
    path('novel/', views.novel_books, name='novel_books'),
    path('novel/add/', views.add_novel_book, name='add_novel_book'),
    path('show/', views.show_books, name='show_books'),
    path('edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete_book'),
]
