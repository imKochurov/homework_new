from datetime import datetime
from django.shortcuts import render

# Create your views here.


# from django.http import HttpResponse
# def index(request):
#     return HttpResponse("Hello! This is my first view.")


def general(request):
    x = datetime.now()
    date = x.strftime('%d-%m-%Y')
    time = x.strftime('%H:%M')
    context = {
        'page_title': 'Моя Django сторінка',
        'welcome_message': 'Вітаю на моїй сторінці!',
        'section_title': 'Основний розділ сторінки',
        'date': date,
        'time': time
    }
    return render(request, 'polls/general.html', context)

def new_page_1(request):
    return render(request, 'polls/new_page_1.html')

def new_page_2(request):
    return render(request, 'polls/new_page_2.html')

def new_page_3(request):
    return render(request, 'polls/new_page_3.html')


# if __name__ == '__main__':
#     x = datetime.datetime.now()
#     date = x.strftime('%d-%m-%Y')
#     print(date)