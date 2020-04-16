from django.conf.urls import url
from app import views

app_name = 'app'

urlpatterns = [
    url(r'^others/',views.others,name='other'),
    url(r'^relative/',views.relative,name='relatives'),
]
