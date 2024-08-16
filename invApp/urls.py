from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-book/', views.createBook, name='add-book'),
    path('all-book/', views.showAllBook, name='all-book'),
    path('book/<int:id>/', views.showBook, name='show-book'),
    path('update-book/<int:id>/', views.updateBook, name='update-book'),
    path('delete-book/<int:id>/', views.deleteBook, name='delete-book')
]