from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from company.models import Question, Exam, Student
import random
import string

def index(request):
    return render(request,'company/index.html')

@login_required
def success(request):
    return render(request,'company/success.html')

def company(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user =authenticate(username=email,password=password)
        if user:
            if user.is_active:
                login(request,user)

                return success(request)

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("Email : {} and password {}".format(email,password))
            return HttpResponse("invalid login details ")
    else:
        if request.user.is_authenticated:
            return success(request)
        else:
            return render(request,'company/company.html',{})

def dashboard(request):
    date_dict={'user': request.user.username}
    return render(request,'company/dashboard.html',context=date_dict)


def add_exam(request):
    if request.method == 'POST':
        try:
            prev_user = Exam.objects.get(user=request.user)
            print prev_user
            return HttpResponse('Already created test')
        except:
            user = request.user.username
            exam = Exam()
            new_n = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            exam.name = new_n
            exam.user = User.objects.get(username=user)
            #print type(exam.user)
            exam.save()
            question1  = request.POST.get("question1")
            option1a = request.POST.get("option1a")
            option1b = request.POST.get("option1b")
            option1c = request.POST.get("option1c")
            option1d = request.POST.get("option1d")
            answer1 = request.POST.get("answer1")
            q1 = Question()
            q1.question = question1
            q1.option1 = option1a
            q1.option2 = option1b
            q1.option3 = option1c
            q1.option4 = option1d
            q1.answer1 = answer1
            print option1a,question1
            q1.exam = Exam.objects.get(user=request.user)
            q1.save()
            question2  = request.POST.get("question2")
            option2a = request.POST.get("option2a")
            option2b = request.POST.get("option2b")
            option2c = request.POST.get("option2c")
            option2d = request.POST.get("option2d")
            answer2 = request.POST.get("answer2")
            q2 = Question()
            q2.question = question2
            q2.option1 = option2a
            q2.option2 = option2b
            q2.option3 = option2c
            q2.option4 = option2d
            q2.answer2 = answer2
            q2.exam = Exam.objects.get(user=request.user)
            q2.save()
            return HttpResponse('success')
    else:
        return render(request,'company/new_quiz.html')


@login_required
def add_student(request):

    if request.method == 'POST':
        name = request.POST.get("student_name")
        email = request.POST.get("student_email")
        added_by = request.user.username
        password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
        s = Student()
        s.name = name
        s.email = email
        s.added_by = added_by
        s.password = password
        s.save()

        return HttpResponse('Successfully added student')
    else:
        return render(request,'company/student.html')
