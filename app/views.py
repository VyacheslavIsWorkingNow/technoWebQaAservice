from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def hot_index(request):
    hot_index_index = True
    context = {'questions': models.QUESTIONS,
               'tags': hot_index_index
               }
    return render(request, 'index.html', context=context)


def tag_index(request, your_tag: str):
    context = {'questions': models.QUESTIONS,
               'tags_other': your_tag
               }
    return render(request, 'index.html', context=context)


def question(request, question_id: int):

    context = {
        'id_questions': models.QUESTIONS[question_id],
        'ans': models.ANS,
    }
    return render(request, 'question.html', context=context)


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def user(request):
    return render(request, 'user_page.html')
