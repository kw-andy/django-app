from django.shortcuts import render,get_object_or_404
from django.template import loader
from django.http import Http404,HttpResponse
from .models import Question

# Crée ta vue ici 

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('enquete/index.html')
    context = {
                'latest_question_list' : latest_question_list
                }
    return render(request, 'enquete/index.html',context)


def detail(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'enquete/detail.html',{'question':question})

def results(request,question_id):
    response = "vous regardez les résultats de la question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return  HttpResponse("Vous votez sur la question  %s." % question_id)
