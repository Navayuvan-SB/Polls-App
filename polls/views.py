from django.http import HttpResponse
from django.shortcuts import render

from .models import Question


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    return HttpResponse("You're looking at results of question %s." % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def index(request):
    recent_five_questions = Question.objects.order_by('-pub_date')[:5]
    context = {
        'recent_five_questions': recent_five_questions
    }

    return render(request, 'polls/index.html', context)
