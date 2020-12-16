from django.shortcuts import render
import requests
import json
import datetime
import re


def response(request):
    now = datetime.datetime.now()
    date_now = "{}-{}-{}".format(now.year, now.month, now.day)
    url = "http://newsapi.org/v2/everything"
    params = {
        'q': 'bitcoin',
        'from': date_now,
        'sortBy': 'publishedAt',
        'apiKey': '1186d3b0ccf24e6a91ab9816de603b90'
    }
    response = requests.request("GET", url, params=params)
    return response


def index(request):
    now = datetime.datetime.now()
    date_now = "{}-{}-{}".format(now.year, now.month, now.day)
    res = response(request)
    # all news
    arr_data = []
    publishedAt = ''
    for news in res.json()['articles']:
        try:
            publishedAt = re.match("\d+-\d+-\d+", news['publishedAt'])
            rm_words = news['content'].split()[:-2]
        except:
            content = None
        else:
            content = " ".join(rm_words)
        data = {
            publishedAt.group(): {
                "source": news['source'],
                "title": news['title'],
                "describe": news['description'],
                "url": news['url'],
                "urlImage": news['urlToImage'],
                "content": content
            }
        }
        arr_data.append(data)

    context = {
        'data': arr_data,
        'date_now': date_now
    }
    return render(request, 'news/news.html', context)