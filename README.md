# quest_master
#установка виртуального окружения
pip install virtualenv

#создание нового каталога
mkdir python-virtual-environments && cd python-virtual-environments
#необходимо активировать виртуальное окружение  для Unix 
source env/bin/activate
#необходимо активировать виртуальное окружение  для windows 
PRG1\Scripts\activate.bat     (RPG1 - название проекта )
#установка django 
pip install django

запуск сервера python manage.py runserver 
в адресной строке браузера вводим данную ссылку http://127.0.0.1:8000/quest/

в данной версии приложения не реализованы DTO объекты и сервис QuizResult
