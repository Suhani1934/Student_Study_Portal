from django.urls import path
from . import views

urlpatterns = [

    # home url
    path('', views.home, name='home'),

    # notes urls
    path('notes/', views.notes, name='notes'),
    path('delete_note/<int:pk>', views.delete_note, name='delete_note'),
    path('notes_detail/<int:pk>',views.NotesDetailView.as_view(), name='notes_detail'),

    # homework urls
    path('homework/', views.homework, name='homework'),
    path('update_homework/<int:pk>', views.update_homework, name='update_homework'),
    path('delete_homework/<int:pk>', views.delete_homework, name='delete_homework'),

    # youtube url
    path('youtube/', views.youtube, name='youtube'),

    # todo urls
    path('todo/', views.todo, name='todo'),
    path('update_todo/<int:pk>', views.update_todo, name='update_todo'),
    path('delete_todo/<int:pk>', views.delete_todo, name='delete_todo'),

    # books url
    path('books/', views.books, name='books'),
    
    # dictionary url
    path('dictionary/', views.dictionary, name='dictionary'),
    
    # wiki url
    path('wiki/', views.wiki, name='wiki'),
    
    # conversion url
    path('conversion/', views.conversion, name='conversion'),
]
