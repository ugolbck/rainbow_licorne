from django.shortcuts import render, get_object_or_404
from mad_licorne.models import Article, Category, Comment
from mad_licorne.forms import CommentForm
from mad_licorne.filters import ArticleFilter

import datetime

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = ArticleFilter(request.GET, queryset=Article.objects.all())
    return render(request, 'index.html', {'latests_articles': articles})


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
    	form = CommentForm(request.POST)
    	if form.is_valid():
    		article.comments.create(name = form.cleaned_data['name'], content = form.cleaned_data['content'], comment_date = datetime.datetime.now())
    form = CommentForm()
    return render(request, 'article.html', {'article': article, 'form': form})


def category(request, slug):
	category = Category.objects.all()
	return render(request, 'article.html', {'category': category})