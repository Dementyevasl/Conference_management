from django.core.paginator import Paginator
from django.shortcuts import render
from django_tables2 import RequestConfig
#from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from geopy.geocoders import GoogleV3, Nominatim
from .tables import ConferenceTable
from .filters import ConferenceFilter
#from notify.signals import notify
import datetime
from datetime import date
import numpy as np
import json
from .models import Conference, Submission, UserConferenceInfo


def status2color(status):
    if status == 'Accepted':
        return "green_circle_little_v2.png"
    elif status == 'Rejected':
        return "red_circle_little_v2.png"
    elif status == 'Pending':
        return "yellow_circle_little_v2.png"
    else:
        return "grey_circle_little_v2.png"

def status2colorday(status):
    if status == 'Accepted':
        return "accepted_day"
    elif status == 'Rejected':
        return "rejected_day"
    elif status == 'Pending':
        return "pending_day"

def status2submissionday(status):
    if status == 'Accepted':
        return "accepted_day_deadline"
    elif status == 'Rejected':
        return "rejected_day_deadline"
    elif status == 'Pending':
        return "pending_day_deadline"

def index(request):
    all_conferences = Conference.objects.all()
    return render(request, 'conference/index.html', {'conferences': all_conferences})

def management_page(request):
    #TO DO: add all stuff needed on managment page
    userConf = UserConferenceInfo.objects.get(pk = request.user.id)
    #current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    #print(current_time)
    if(request.GET.get('StatusChangerBtn')):
        conf_id = int(request.GET.get('conf_id'))
        conf_status = request.GET.get('submission_status')
        conference_to_change =  Conference.objects.get(pk=conf_id)
        Submission_to_change = Submission.objects.get(user = request.user.id, conference = conference_to_change)
        Submission_to_change.status = conf_status
        Submission_to_change.save()

    if(request.GET.get('DeleteSubmissionBtn')):
        conf_id = int(request.GET.get('conf_id'))
        conference_adjusted =  Conference.objects.get(pk=conf_id)
        Submission_to_delete = Submission.objects.get(user = request.user.id, conference = conference_adjusted).delete()
        conference_adjusted.isRegistered = False
        conference_adjusted.save()


    user_submissions = Submission.objects.filter(user = request.user.id)
    status_choices = [x[1] for x in Submission.status_choices]
    submission_conf_ids = [x.conference.id for x in user_submissions]

    # SUGGESTION TABLE PART

    if(request.GET.get('SuggestUpdaterBtn')):
        #implement picking of random numbers from conf ids
        all_conferences_id = [x.id for x in Conference.objects.all() if (x.dates_start != None) and (x.dates_start > date.today())]
        random_suggestions = np.random.choice(all_conferences_id, 12, replace = False)
        userConf.set_suggestions(np.setdiff1d(random_suggestions, submission_conf_ids).tolist())
        userConf.save()

    if(request.GET.get('SuggestDeleterBtn')):
        userConf.suggestions = None
        userConf.save()
    
    if userConf.suggestions == None:
        user_suggestions = None
        suggestion_table = None
    else:
        suggested_conf_ids = userConf.get_suggestions()
        user_suggestions = Conference.objects.filter(id__in = suggested_conf_ids)
        suggestion_table = ConferenceTable(Conference.objects.filter(id__in = suggested_conf_ids))
        RequestConfig(request, paginate={'per_page': 10}).configure(suggestion_table)

    
    # GOOGLE MAP PART
    geolocator = Nominatim()

    user_submission_marks_info = [(f"{x.conference.location_country} {x.conference.location_city}",x.conference.confTitle,x.status) for x in user_submissions]
    
    if userConf.suggestions != None:
        user_submission_marks_info.extend([(f"{x.location_country} {x.location_city}",x.confTitle, "Suggested") for x in user_suggestions])

    # Get rid of None locations (they won't be displayed)
    #print(user_submission_marks_info)
    user_submission_marks_info = [x for x in user_submission_marks_info if "None" not in x[0]]
    #print('------------')
    #print(user_submission_marks_info)

    icon_links = [status2color(x[2]) for x in user_submission_marks_info]
    marks_geoposition = [geolocator.geocode(x[0]) for x in user_submission_marks_info]
    marks_title = [x[1] for x in user_submission_marks_info]

    user_submission_marks_info = list(zip(icon_links, marks_geoposition, marks_title))
    user_submission_marks_info = [x for x in user_submission_marks_info if x[1] != None]
    user_submission_marks_info = [x for x in user_submission_marks_info if (type(x[1].latitude) is float) and (type(x[1].longitude) is float)]
    print(len(user_submission_marks_info))
    
    #CALENDAR PART

    if user_submissions == None:
        conference_date_info = None
    else:
        subm_confs = [x.conference for x in user_submissions]
        subm_confs_deadline = [x.conference for x in user_submissions if x.conference.paperDeadline != None]
        user_submission_deadline = [x for x in user_submissions if x.conference.paperDeadline != None]
        conference_dates_start = [x.dates_start.strftime('%Y-%m-%d') for x in subm_confs]
        conference_dates_deadline = [x.paperDeadline.strftime('%Y-%m-%d') for x in subm_confs_deadline]
        date_start_class = [status2colorday(x.status) for x in user_submissions]
        date_deadline_class = [status2submissionday(x.status) for x in user_submission_deadline]
        conference_dates_start_tooltips = [f"Start day for conference: {x.confTitle}" for x in subm_confs]
        conference_dates_deadline_tooltips = [f"Paper Submission deadline for conference: {x.confTitle}" for x in subm_confs_deadline ]
        conference_date_info = list(zip(conference_dates_start, date_start_class, conference_dates_start_tooltips))
        conference_date_info.extend(list(zip(conference_dates_deadline, date_deadline_class, conference_dates_deadline_tooltips)))
        #print(conference_date_info) 
    
    #UPCOMING CONFERENCE PART

    accepted_conf_title = [x.conference.confTitle for x in user_submissions if x.status == Submission.ACCEPTED]
    accepted_conf_date = [x.conference.dates_start.strftime('%m/%d/%Y') for x in user_submissions if x.status == Submission.ACCEPTED]
    accepted_conf = list(zip(accepted_conf_title, accepted_conf_date, [Submission.ACCEPTED] * len(accepted_conf_title)))

    if userConf.suggestions == None:
        upcoming_conferences = accepted_conf
    else:
        user_suggestions_title = [x.confTitle for x in user_suggestions]
        user_suggestions_date = [x.dates_start.strftime('%m/%d/%Y') for x in user_suggestions]
        accepted_conf.extend(list(zip(user_suggestions_title, user_suggestions_date, ['Suggested'] * len(user_suggestions))))
    
    accepted_conf.sort(key=lambda x: datetime.datetime.strptime(x[1], '%m/%d/%Y'))
    upcoming_conferences = accepted_conf[:3]

    context = {
        'userConferenceInfo': user_submissions,
        'status_choices':status_choices,
        'submission_conf_ids':submission_conf_ids,
        'user_suggestions': user_suggestions,
        'suggestion_table': suggestion_table,
        'upcoming_conferences': upcoming_conferences,
        'marks_info': user_submission_marks_info,
        'dates_info': conference_date_info
    }

    return render(request, 'conference/management_page.html', context= context)

def detail(request, conference_id):
    conference = Conference.objects.get(pk=conference_id)
    if(request.GET.get('SubmissionBtn')):
        userConf = UserConferenceInfo.objects.get(pk = request.user.id)
        submission = Submission(user = userConf, conference = conference)
        conference.isRegistered = True
        conference.save()
        submission.save()
    return render(request, 'conference/conference.html', {'conference': conference})


def listing(request):
    conference_list = Conference.objects.all()
    paginator = Paginator(conference_list, 25) # Show 25 contacts per page

    page = request.GET.get('page')
    conferences = paginator.get_page(page)
    return render(request, 'conference/index.html', {'conferences': conferences})

# class FilteredConferenceListView(SingleTableMixin, #):
#     table_class = ConferenceTable
#     model = Conference
#     template_name = 'template.html'

#     filterset_class = ConferenceFilter