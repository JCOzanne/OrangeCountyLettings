"""
This module defines views for the profiles app.
It includes views for the index page and the profile page.
"""
import logging
from django.shortcuts import render, get_object_or_404
from sentry_sdk import capture_exception
from .models import Profile

logger = logging.getLogger(__name__)


def index(request):  # ancien profiles_index
    """
    Renders the index page with a list of all profiles.
    Retrieves all Profile objects and passes them to the template for display.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template profiles/index.html
    """
    logger.info("Rendu de la page d'accueil des profiles")
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    Renders the profile page for a specific user.
    Retrieves the Profile object associated with the given username
    and passes it to the template for display.
    :param request: instance of HttpRequest
    :param username: username of profile
    :return: HttpResponse with rendered template profiles/profile.html
    """
    logger.info(f"Accès au profil de l’utilisateur : {username}")
    try:
        profile = get_object_or_404(Profile, user__username=username)
    except Exception as e:
        logger.exception(f"Erreur lors de la récupération du profil : {username}")
        capture_exception(e)
        return render(request, "500.html", status=500)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
