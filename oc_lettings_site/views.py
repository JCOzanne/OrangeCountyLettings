from django.shortcuts import render


def index(request):
    """
    Renders the home page.
    This view simply renders the 'index.html' template.
    :param request: instance of HttpRequest
    :return: HttpResponse with rendered template index.html
    """
    return render(request, 'index.html')
