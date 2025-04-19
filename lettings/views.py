from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):  # ancien lettings_index
    """
    Renders the index page with a list of all lettings.
    Retrieves all Letting objects and passes them to the template for display.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template lettings/index.html
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


def letting(request, letting_id):
    """
    Renders the letting details page for a specific letting.
    Retrieves the Letting object with the given ID and passes it to the template for display.
    :param request: instance of HttpRequest
    :param letting_id: id of letting
    :return: HttpResponse with rendered template lettings/letting.html
    """
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'letting': letting,
    }
    return render(request, 'lettings/letting.html', context)
