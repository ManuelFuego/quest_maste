from django.urls import path
from .views import start_test, add_message, about, testpage, result, save

urlpatterns = [
    path('', start_test, name='test_page'),
    path('add_message', add_message, name='add_message'),
    path('about', about, name='about'),
    path('testpage', testpage, name='testpage'),
    path('result', result, name='result'),
    path('save', save, name='save'),

]
