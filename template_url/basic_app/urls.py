from django.conf.urls import url
from basic_app import views
#template tagging for url

app_name='basic_app'
#after domain_name/basic, use these url routes
urlpatterns=[
url(r'^relative/',views.relative,name='relative'),
url(r'^other/',views.other,name='other'),

]
