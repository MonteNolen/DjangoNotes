from django.contrib import admin
from .models import NoteAuthor, Note

class Notes(admin.TabularInline):
    model = Note
    extra = 0

class NoteAuthorAdmin(admin.ModelAdmin):
    inlines = [Notes]

admin.site.register(NoteAuthor, NoteAuthorAdmin)

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_filter = ('user', 'status', 'created')
    list_display = ('title', 'user', 'status', 'created')
    fieldsets = (
        # (None, { 
        #     'fields': ('note', 'id')
        # }),
        ('Availability', {
            'fields': ('title', 'user', 'textarea', 'status')
        }),
    )
