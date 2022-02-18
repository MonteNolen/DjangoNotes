from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from .forms import *

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
    #paginate_by = 20
    def get_queryset(self):
        return Note.objects.all()


class NoteUpdate(UpdateView):
    model = Note
    fields = ['user','textarea']
    template_name = 'notes/note_form.html'
    success_url = reverse_lazy('notes')

    def dispatch(self, *args, **kwargs):
        self.note_id = kwargs['pk']
        return super(NoteUpdate, self).dispatch(*args, **kwargs)
    
    def form_valid(self, form):
        form.save()
        note = Note.objects.get(id=self.note_id)
        return super(NoteUpdate, self).form_valid(form)
        


class NoteCreate(CreateView):
    model = Note
    fields = ['user','textarea']
    success_url = reverse_lazy('notes')
    template_name = 'notes/create.html'

    def form_valid(self, form):
        form.save()
        return super(NoteCreate, self).form_valid(form)
