from django.urls import path

from . import views
from .views import NoteCreate, NoteListView, NoteDetailView, MyNoteListView, NoteUpdateView, NoteDeleteView

urlpatterns = [
    path('create/', NoteCreate.as_view(), name='create_note'),
    path('list/', NoteListView.as_view(), name='list_note'),
    path('my-list/', MyNoteListView.as_view(), name='my_notes'),
    path('<slug:slug>/', NoteDetailView.as_view(), name='note-detail'),
    path('update/<slug:slug>/', NoteUpdateView.as_view(), name='note-update'),
    path('delete/<slug:slug>/', NoteDeleteView.as_view(), name='note-delete'),
]