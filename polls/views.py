from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Question


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


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
