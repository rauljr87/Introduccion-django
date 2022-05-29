# Class-based generic views

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import UpdateView, DeleteView
from .forms import PostCreateForm
# Para crear Post declarado en el modelo
from .models import Post
# Para redireccionar vista de update
from django.urls import reverse_lazy


# Indice del blog
# Todos los post que existen
class BlogListView(View):
    """ Vista para blog_list """

    def get(self, request, *args, **kwargs):
        # Llamando a todos los objetos POST que se encuentran en la base de datos
        posts = Post.objects.all()
        # Visualizar los objetos POST
        context = {
            'posts': posts
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


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        """ Muestra detalle de un solo Post a través de su pk"""

        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog_detail.html', context)


class BlogUpdateView(UpdateView):
    """ Actualiza un post """

    model = Post
    fields = ['title', 'content']
    template_name = 'blog_update.html'

    # Redireccionando a blog_list
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})


class BlogDeleteView(DeleteView):
    """ Elimina un post """

    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')
