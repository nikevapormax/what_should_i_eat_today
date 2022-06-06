import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [{'name': '족발', 'price': 35000}, {'name': '햄버거', 'price': 9000}, {'name': '치킨', 'price': 18000}, {'name': '삼겹살', 'price': 12000}]
    pick = random.choice(menus)
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
    }
    return render(request, 'dinner.html', context)


def review(request):
    return render(request, 'review.html')


def create_review(request):
    content = request.POST.get('content')
    print(content)
    context = {
        'content': content,
    }
    
    return render(request, 'review_result.html', context)