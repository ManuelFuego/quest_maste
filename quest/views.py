from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from .models import Answer
from collections import defaultdict
from .forms import *
from .models import *


def question_list(request):
    '''
    paginator = Paginator(questions,1)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    answers = Answer.objects.all()

    '''
    quest = Answer.objects.all()
    paginator = Paginator(quest, 1)
    page_num = request.GET.get('page')
    questions = paginator.get_page(page_num)
    # return render(request, 'quest/index.html',context={'page_obj':page_obj, 'answers':answers})
    return render(request, 'quest/index.html', context={'questions': questions})


def add_test(request):
    if request.method == 'POST':
        form = AddTest(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddTest()
    return render(request, 'quest/add_test.html', {'form': form})


def about(request):
    return render(request, 'quest/about.html')


def test_number_one(request):
    quest = Question.objects.all()
    answers = Answer.objects.all()
    s = []
    for q in quest:
        test = {
            'quest': q.question
        }
        listA = []
        for a in answers:
            if a.question == q:
                listA.append(a.answer)
        test['answers'] = listA
        s.append(test)

    context = {'question': s}
    return render(request, 'quest/test_number_one.html', context)
