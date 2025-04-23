import logging
from django.shortcuts import render, get_object_or_404
from sentry_sdk import capture_exception
from .models import Letting

logger = logging.getLogger(__name__)


def index(request):  # ancien lettings_index
    """
    Renders the index page with a list of all lettings.
    Retrieves all Letting objects and passes them to the template for display.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template lettings/index.html
    """
    logger.info("Rendu de la page d'accueil des locations")
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
    logger.info(f"Accès à la page détail d’une location (ID={letting_id})")
    try:
        letting = get_object_or_404(Letting, id=letting_id)
    except Exception as e:
        logger.exception(f"Erreur lors du chargement de l'ID de la location={letting_id}")
        capture_exception(e)
        return render(request, "500.html", status=500)
    context = {'letting': letting}
    return render(request, 'lettings/letting.html', context)
