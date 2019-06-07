from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Conference


def index(request):
    all_conferences = Conference.objects.all()
    return render(request, 'conference/index.html', {'conferences': all_conferences})


def detail(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    return render(request, 'conference/conference.html', {'conference': conference})


def listing(request):
    conference_list = Conference.objects.all()
    paginator = Paginator(conference_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    conferences = paginator.get_page(page)
    return render(request, 'conference/index.html', {'conferences': conferences})