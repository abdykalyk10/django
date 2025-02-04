import datetime
from datetime import datetime
from django.http import HttpResponse


def about_me(request):
    if request.method == "GET":
        return HttpResponse("Меня зовут Абдыкалык <br> Мне 19 лет")


def text_and_photo(request):
    if request.method == "GET":
        return HttpResponse(
            "<h1>Море по ночьным небом</h1><img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQBF__6AaGPAMd4ha0VpqmSxwf8_XM6N_wWvQ&s'>")


def system_time(request):
    if request.method == "GET":
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f"Текущее время: {current_time}")
