from django import forms
from .models import Post


# Declarando formulario
class PostCreateForm(forms.ModelForm):
    # class Meta para declarar el formulario que queremos editar
    class Meta:
        model = Post
        fields = ('title', 'content')
