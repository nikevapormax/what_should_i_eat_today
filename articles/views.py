import random
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = [{'name': '족발', 'price': 35000}, {'name': '햄버거', 'price': 9000}, {'name': '치킨', 'price': 18000}, {'name': '삼겹살', 'price': 12000}]
    pick = random.choice(menus)
    articles = Article.objects.order_by('-pk')
    context = {
        'pick': pick,
        'name': name,
        'menus': menus,
        'articles': articles,
    }
    return render(request, 'dinner.html', context)


def review(request):
    return render(request, 'review.html')


def create_review(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    
    return redirect('/articles/dinner/messi')