from django.db import models


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
