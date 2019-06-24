from django.db import models
from django.contrib.auth.models import User
import datetime
import json

class Conference(models.Model):
    confTitle = models.CharField(max_length=100)
    confFamily = models.CharField(max_length=100, blank=True, null=True)
    location_country = models.CharField(max_length=100, blank=True, null=True)
    location_city = models.CharField(max_length=100, blank=True, null=True)
    dates_start = models.DateField(blank=True, null=True)
    dates_end = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    contacts_email = models.EmailField(blank=True, null=True)
    contacts_phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    acceptance_rate = models.FloatField(blank=True, null=True)
    impact_factor = models.FloatField(blank=True, null=True)
    sponsors = models.TextField(blank=True, null=True)
    paperDeadline = models.DateField(blank=True, null=True)
    pageNumber_min = models.IntegerField(blank=True, null=True)
    pageNumber_max = models.IntegerField(blank=True, null=True)
    pageNumber_ave = models.FloatField(blank=True, null=True)
    field = models.TextField(blank=True, null=True)
    isRegistered = models.BooleanField(default=False)

    def get_fields(self):
        if not self.field:
            return self.field
        return self.field.split(',')

    def get_sponsors(self):
        if not self.sponsors:
            return self.sponsors
        return self.sponsors.split(',')

class UserConferenceInfo(models.Model):

    user =  models.OneToOneField(User, on_delete= models.CASCADE)

    submissions = models.ManyToManyField(Conference, through='Submission')

    suggestions = models.CharField(max_length=200, null = True)

    def set_suggestions(self, x):
        self.suggestions = json.dumps(x)

    def get_suggestions(self):
        return json.loads(self.suggestions)

    def __str__(self):
	    return self.user.username

class Submission(models.Model):
    user = models.ForeignKey(UserConferenceInfo, on_delete= models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete= models.CASCADE)
    data_creation = models.DateField(default=datetime.date.today)
    data_last_update = models.DateField(default=datetime.date.today)
    ACCEPTED = 'Accepted'
    REJECTED = 'Rejected'
    PENDING  = 'Pending'

    status_choices = [
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
        (PENDING, 'Pending')
    ]
    
    status = models.CharField(max_length = 10, choices = status_choices, default= PENDING)

    def __str__(self):
        return f"Conference_ID: {self.conference.id}, Conference_Name: {self.conference.confTitle}, Status: {self.status}"