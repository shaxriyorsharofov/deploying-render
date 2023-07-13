from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import News
# Create your views here.


class NewsList(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = News
    template_name = 'detail.html'
    context_object_name = 'detail'
