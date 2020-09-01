from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é show de bolinha dms'
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
