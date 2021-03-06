from django.contrib import admin
from django.urls import path
from django.urls import include
# Llamamos de views la clase HomeViews
# . , hace referencia al mismo folder raíz del archivo urls.py
from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),

    # as_view, para cuando llamamos a una clase
    # '', redireccionamos la vista principal
    path('', HomeView.as_view(), name="home"),

    # mapeo de App blog
    path('blog/', include('blog.urls', namespace='blog'))
]
