# Vistas de clases
from django.views.generic import View
from django.shortcuts import render


class HomeView(View):
    """ Acceso a get request y post request """

    # Llamar, get request, pide (obtener) la información para poder ver
    # post request, información que se envía para mandar al servidor para que haga algo con dicha info
    def get(self, request, *args, **kwargs):
        # template, código HTML
        context = {

        }
        return render(request, 'index.html', context)
