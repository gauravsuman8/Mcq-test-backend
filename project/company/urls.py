from django.conf.urls import url
from . import views
#from django.urls import path

app_name = 'company'

urlpatterns = [
    url(r'^$',views.company, name="user_login"),
    #url(r'^success/$',views.success,name="success"),
    url(r'^success/$',views.success,name='success'),
    url(r'^dashboard/$',views.dashboard,name='dashboard'),
    url(r'^new_quiz/$',views.add_exam,name='new_quiz'),
    url(r'^add_question/$',views.add_question,name='add_question'),
    url(r'^add_student/$',views.add_student,name='add_student'),
    #url(r'^test/(?P<id>(.*?))/$',views.test),
]
