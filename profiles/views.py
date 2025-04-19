from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):  # ancien profiles_index
    """
    Renders the index page with a list of all profiles.
    Retrieves all Profile objects and passes them to the template for display.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template profiles/index.html
    """
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
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
