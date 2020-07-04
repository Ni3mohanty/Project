from rest_framework import serializers 
from api.models import User, ActivityPeriod

class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'real_name',
                  'tz')


class ActivityPeriodSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ActivityPeriod
        fields = (
                  'start_time',
                  'end_time')