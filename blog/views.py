from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.
# Indice del blog
# Todos los post que existen
class BlogListView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_list.html', context)