from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def hot_index(request):
    return HttpResponse(f' tag = hooot')


def tag_index(request, your_tag: str):
    return HttpResponse(f'tag = {your_tag}')


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
