import re

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *

def start_test(request):
    return render(request, 'quest/index.html')

def add_message(request):
    if request.method == 'POST':
        form = Addmessage(request.POST)
        if form.is_valid():
            form.save()
            form = Addmessage()
    else:
        form = Addmessage()
    show_message = Message.objects.order_by('-date_pub')
    paginator = Paginator(show_message, 3)
    page = int(request.GET.get('page','1'))
    message = paginator.page(page)
    return render(request, 'quest/message.html', {'form': form,'message':message})

def about(request):
    return render(request, 'quest/about.html')

answerlist = []
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
                listA.append(a)
        test['answers'] = listA
        s.append(test)
    paginator = Paginator(s, 1)
    page = int(request.GET.get('page', '1'))
    pages = paginator.page(page)
    context = {'page': pages}
    return render(request, 'quest/test_number_one.html', context)

def save(request):
    ''' для подсчета'''
    answer = request.GET['answer']
    answerlist.append(answer)
    return render(request, 'quest/test_number_one.html')

uuidlist = []           # лист uuid с его помощью вытягиваем ответы пользователя
trues_list = []         # лист тру считаем ответы
user_choice = []        # здесь хранятся ответы
def result(request):
    scope = 0
    for i in answerlist:
        uuidlist.append(re.findall((r'^(.+?)\@'),i))
    for u in uuidlist:
        for n in u:
            user_ans = Answer.objects.filter(answer_uuid=n).values_list('answer')
            user_choice.append(user_ans)


    for t in answerlist:
        trues_list.append(re.findall((r'@(.*)'), t))
    for b in trues_list:
        for a in b :
            if 'True' in a :
                scope += 1
    try:
        scope = scope/len(answerlist)
    except ZeroDivisionError:
            return render(request, 'quest/index.html')
    context = {'scope': scope, 'user_choice':user_choice}
    return render(request, 'quest/result.html', context)

