from django.conf.urls import url
from . import views
#from django.urls import path

app_name = 'student'

urlpatterns = [
    url(r'^$',views.student, name="student_login"),
]
