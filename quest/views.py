import re
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
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
def testpage(request):
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
    return render(request, 'quest/testpage.html', context)

def save(request):
    ''' для подсчета'''
    answer = request.GET['answer']
    answerlist.append(answer)
    return render(request, 'quest/testpage.html')

uuidlist = []           # лист uuid с его помощью вытягиваем ответы пользователя
trues_list = []         # лист тру для подсчета количества правильных ответов
user_choice = []        # для вывода выбранных пользователем ответов

def result(request):
    score = 0
    for i in answerlist:
        uuidlist.append(re.findall((r'^(.+?)\@'),i))
    for u in uuidlist:
        for n in u:
            user_ans = Answer.objects.filter(answer_uuid=n).values_list('answer', flat=True)
            user_choice.append(user_ans)


    for t in answerlist:
        trues_list.append(re.findall((r'@(.*)'), t))
    for b in trues_list:
        for a in b :
            if 'True' in a:
                score += 1
    try:
        score = score/len(answerlist)
    except ZeroDivisionError:
            score= 0
            return render(request, 'quest/result.html',context={'score':score})
    context = {'score': score * 100, 'user_choice': user_choice}
    return render(request, 'quest/result.html', context)

