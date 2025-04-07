from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages

from news.models import Article
from .forms import ArticleForm

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = ArticleForm()
    return render(request, 'news/create_article.html', {'form': form})

def get_post(request):
    if request.method == "POST":
        print("POST")
    else:
        news_obj= Article.objects.filter(status=1).order_by('-id')[:3]
        return render(request, 'news/display_news.html', {'news_obj': news_obj})

def get_post_id(request,id):
    if request.method == "POST":
        print("POST")
    else:
        try:
            news_obj= Article.objects.get(id=id,status=1)
        except Article.DoesNotExist:
            messages.success(request,"Article not found or not active.")
            return render(request, 'news/detail_display_news.html', {'news_obj': None})
        return render(request, 'news/detail_display_news.html', {'news_obj': news_obj})