from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.NoteListView.as_view(), name='notes'),
    path('note/<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('note/<int:pk>/note-edit/', views.NoteUpdate.as_view(), name='note-edit'),
    path('note/create', views.NoteCreate.as_view(), name='create'),
]