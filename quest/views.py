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
            form= Addmessage()
    else:
        form = Addmessage()
    return render(request, 'quest/message.html', {'form': form})

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

def saveall(request):
    answer = request.GET['answer']
    alllist=[]
    alllist.append(answer)
    #return render(request, 'quest/test_number_one.html')

ans = []
def save(request):
    answer = request.GET['answer']
    answerlist.append(answer)
    return render(request, 'quest/test_number_one.html')

def result(request):
    scope = 0
    for i in answerlist:
        if i == 'True':
            scope += 1
    if len(answerlist) != 0:
        scope = 0
    else:
        try:
            scope = scope/len(answerlist)
        except ZeroDivisionError:
            return render(request, 'quest/index.html')
    context = {'scope': scope/len(answerlist)}
    return render(request, 'quest/result.html', context)
