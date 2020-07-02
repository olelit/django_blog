from django.forms import ModelForm

from notepad.note.models import Note


class ArticleForm(ModelForm):
    class Meta:
         model = Note
         fields = ['title', 'body']