from django import forms
from tinymce.widgets import TinyMCE
from .model import Note

class NoteEditForm(ModelForm):
    
    textarea = forms.TextareaField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Note
        # fields = '__all__'