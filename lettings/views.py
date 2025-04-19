from django.shortcuts import render, get_object_or_404
from .models import Letting

def index(request):  # ancien lettings_index
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)

def letting(request, letting_id):
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'letting': letting,
    }
    return render(request, 'lettings/letting.html', context)
