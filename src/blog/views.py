from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Article, Category, Comment



def home(request):
    articles = (
        Article.objects
        .filter(is_published=True)
        .order_by('-publication_date')[:3]
    )
    return render(request, 'home.html', {'articles': articles})



def article_list(request):
    articles = (
        Article.objects
        .filter(is_published=True)
        .order_by('-publication_date')
    )
    return render(request, 'article_list.html', {'articles': articles})



def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article).order_by('-publication_date')

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments
    })


# Список категорий
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
