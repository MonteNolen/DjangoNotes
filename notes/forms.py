from django import forms
from .models import Note

class NoteForm(forms.Form):
    model = Note
    status = forms.CharField(label='Поставьте галочку, если задача закрыта')