from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import json
from datetime import datetime
import itertools

with open(settings.NEWS_JSON_PATH, 'r') as f:
    news_list = json.load(f)

news_list.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)


def simple_date_fun(date):
    return datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

all_news = [{'date': date, 'values': list(news)} for date, news in
            itertools.groupby(news_list, lambda x: simple_date_fun(x['created']))]


def home(request):
    return redirect('/news')


def index(request):
    # print(request.GET.get('search'))
    if request.GET.get('q', None):
        searched = request.GET.get('q')
        # print(searched)
        filtered_news_list = list(filter(lambda x: searched in x['title'], news_list))
        # print(filtered_news_list)
        # print(news_list)
        all_news = [{'date': date, 'values': list(news)} for date, news in itertools.groupby(filtered_news_list, lambda x: simple_date_fun(x['created']))]
    else:
        all_news = [{'date': date, 'values': list(news)} for date, news in itertools.groupby(news_list, lambda x: simple_date_fun(x['created']))]
    context = {'news': all_news}
    return render(request, 'news/news.html', context)


def detail(request, news_id):
    context = None
    for item in news_list:
        if news_id == item['link']:
            context = {'news': item}
    return render(request, 'news/detail.html', context)


def create(request):
    if request.method == "POST":
        new = dict()  # {"created": "", "text": "", "title": "", "link": 0}
        new['created'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        new['text'] = request.POST.get('text')
        new['title'] = request.POST.get('title')
        new['link'] = len(news_list) + 1
        news_list.append(new)
        news_list.sort(key=lambda x: datetime.strptime(x['created'], "%Y-%m-%d %H:%M:%S"), reverse=True)
        with open(settings.NEWS_JSON_PATH, 'w') as file:
            json.dump(news_list, file, indent=4)
        global all_news
        all_news = [{'date': date, 'values': list(news)} for date, news in
                    itertools.groupby(news_list, lambda x: simple_date_fun(x['created']))]
        return redirect('/news')
    context = None
    return render(request, 'news/create.html', context)
