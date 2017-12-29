from django.conf.urls import url
from student import views
#from django.urls import path

app_name = 'student'

urlpatterns = [
    url(r'^$',views.student_login, name="student_login"),
    url('test/',views.quest,name='tst'),
    #url(r'^test/(?P<id>(.*?))/$',views.quest),
]
