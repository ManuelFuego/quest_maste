from django.urls import path
from .views import start_test, add_message, about, test_number_one, result, save

urlpatterns = [
    path('', start_test, name='test_page'),
    path('add_message', add_message, name='add_message'),
    path('about', about, name='about'),
    path('test_number_one', test_number_one, name='test_number_one'),
    path('result', result, name='result'),
    path('save', save, name='save'),

]
