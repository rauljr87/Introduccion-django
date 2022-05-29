from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .forms import PostCreateForm
# Para crear Post declarado en el modelo
from .models import Post


# Indice del blog
# Todos los post que existen
class BlogListView(View):
    """ Vista para blog_list """

    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'blog_list.html', context)


class BlogCreateView(View):
    """ Vista para crear formulario PostCreateForm """

    # Solicitando información
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)

    # Enviando información
    def post(self, request, *args, **kwargs):
        # Si el método es POST
        if request.method == "POST":
            # Pedir el formulario
            form = PostCreateForm(request.POST)
            # Si el formulario es válido
            if form.is_valid():
                # Obtener
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                # Crear POST
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()

                # Redireccionando a la página blog_list
                return redirect('blog:home')

        context = {

        }
        return render(request, 'blog_create.html', context)
