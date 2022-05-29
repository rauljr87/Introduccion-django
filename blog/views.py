from django.shortcuts import render
from django.views.generic.base import View
from .forms import PostCreateForm


# Create your views here.
# Indice del blog
# Todos los post que existen
class BlogListView(View):
    """ Genera página para blog_list """

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    """ Vista para formulario PostCreateForm """

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_create.html', context)