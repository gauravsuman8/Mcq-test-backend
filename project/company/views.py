from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from company.models import Question, Exam
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
            return render(request,'company/new_quiz.html')

def add_question(request):
        question  = request.POST.get("question")
        option1 = request.POST.get("option1")
        option2 = request.POST.get("option2")
        option3 = request.POST.get("option3")
        option4 = request.POST.get("option4")
        answer = request.POST.get("answer")
        q = Question()
        q.question = question
        q.option1 = option1
        q.option2 = option2
        q.option3 = option3
        q.option4 = option4
        q.answer = answer
        q.exam = Exam.objects.get(user=request.user)
        q.save()
        return HttpResponse("success")
