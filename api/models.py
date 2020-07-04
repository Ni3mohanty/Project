
from django.db import models
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
# Create your models here.
class User(models.Model):
    
    real_name = models.CharField(max_length=70, blank=False, default='')
    tz = models.CharField(max_length=64, choices=TIMEZONES, default='UTC')


class ActivityPeriod(models.Model):
    user = models.ForeignKey(User, related_name='activity', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()