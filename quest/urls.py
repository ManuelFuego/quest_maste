from django.urls import path
from .views import question_list, add_test, about

urlpatterns = [
    path('',question_list , name= 'test_page'),
    path('add_test',add_test, name='add_test'),
    path('about', about, name='about'),

]


