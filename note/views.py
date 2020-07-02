from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.template.defaultfilters import slugify

from .models import Note


class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'image', 'body']
    success_url = "/note/list/"

    def form_valid(self, form):
        form.instance.author_id = self.request.user
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)


class NoteListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        queryset = Note.objects.filter(is_published=True)
        return queryset


class MyNoteListView(ListView):
    paginate_by = 10
    template_name = 'note/my_note_list.html'

    def get_queryset(self):
        queryset = Note.objects.filter(author_id=self.request.user)
        return queryset


class NoteDetailView(DetailView):
    model = Note


class NoteUpdateView(UpdateView):
    fields = ['title', 'image', 'body']
    model = Note
    success_url = "/note/my-list/"


class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/note/my-list/"
