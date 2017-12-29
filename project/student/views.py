# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from company.models import Student,Question,Exam
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

def student_login(request):
    #print 'yes'
    if request.method == 'POST':
        email = request.POST.get("stud_email")
        password = request.POST.get("stud_pass")
        obj = Student.objects.get(email=email)
        added_by = obj.added_by
        if obj:
            date_dict={'stud_email': email, 'company': added_by}
            request.session['stud_email']=email
            request.session['added_by']=added_by
            return HttpResponseRedirect('test')
        else:
            return HttpResponse('Invalid cridentials')

    else:
        return render(request,'student/student_login.html')

def quest(request):
    by=str(request.session['added_by'])
    x = Exam.objects.all()
    exam_name=""
    for y in x:
        if str(y.user) == by:
            exam_name=y
            break
    x = Question.objects.all()
    l=[]
    for y in x:
        if y.exam == exam_name:
            l.append(y)
    if not l:
        return HttpResponse('You are not allowed to attend this test')
    for x in l:
        print x.question
    return render(request,'student/test.html',{'lis' : l})
