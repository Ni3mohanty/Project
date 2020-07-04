from django.conf.urls import url 
from .views import user_list, user_detail, user_activity
 
urlpatterns = [ 
    url('nitin/api/activity', user_activity),
   
    
    
]