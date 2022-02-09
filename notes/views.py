from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import NoteAuthor, Note

def index(request):
    return render(
        request,
        'notes/index.html',
        context = {
            'title': 'Главная страница',
            }
    )

class NoteDetailView(generic.DetailView):
    model = Note

class NoteListView(generic.ListView):
    model = Note
    template_name = 'notes/note_list.html'
    paginate_by = 20

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'textarea', 'status']
    success_url = reverse_lazy('notes')
    template_name = 'notes/create.html'
    

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'textarea', 'status']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes')
    
