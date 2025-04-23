import logging
from django.shortcuts import render
from sentry_sdk import capture_exception

logger = logging.getLogger(__name__)

def index(request):
    """
    Renders the home page.
    This view simply renders the 'index.html' template.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template index.html
    """
    logger.info("Rendu de la page d'accueil")
    return render(request, 'index.html')


def warning_404(request, exception):
    logger.warning(f"Erreur 404 - page non trouvée : {request.path}")
    capture_exception(exception)
    return render(request, "404.html", status=404)

def error_500(request):
    logger.error("Erreur 500 - internal server error")
    capture_exception(Exception("Internal server error"))
    return render(request, "500.html", status=500)

def trigger_key_error(request):
    logger.error("Erreur KeyError volontaire pour tester page 500")
    my_dict = {"clé": "valeur"}
    return my_dict["autre_clé"]