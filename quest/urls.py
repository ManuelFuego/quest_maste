from django.urls import path
from .views import question_list, add_test, about, test_number_one, result, save

urlpatterns = [
    path('', question_list, name='test_page'),
    path('add_test', add_test, name='add_test'),
    path('about', about, name='about'),
    path('test_number_one', test_number_one, name='test_number_one'),
    path('result', result, name='result'),
    path('save', save, name='save'),

]
