from django.shortcuts import render
from .models import Conference

# Create your views here.
def index(request):
    all_conferences = Conference.objects.all()
    return render(request, 'conference/index.html', {'conferences': all_conferences})

def detail(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    return render(request, 'conference/conference.html', {'conference': conference})