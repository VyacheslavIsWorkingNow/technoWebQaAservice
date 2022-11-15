from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET

# TODO: сделать все вьюхи и шаблоны

def index(request):
    return render(request, 'index.html')


def hot_index(request):
    return HttpResponse(f' tag = hooot')


def tag_index(request, your_tag: str):
    return HttpResponse(f'tag = {your_tag}')


def question(request, question_id: int):
    questions = []
    for i in range(1, 30):
        questions.append({
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        })
    return HttpResponse(f'question id = {question_id}')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def ask(request):
    return render(request, 'ask.html')


def user(request):
    return render(request, 'user_page.html')
