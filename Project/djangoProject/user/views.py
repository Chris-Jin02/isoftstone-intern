import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from user.models import *
import json
def getkeywords(request):
    keywordsList= keywords.objects.values('frequency')
    # print(provinceAndConfirmedList)
    from utils import querySetToJson
    res = querySetToJson(keywordsList.values())
    return HttpResponse(res, content_type='application/json')


def get_total(request):
    queryset = total.objects.values('date', 'Paper_Num', 'subject')

    data = {}
    for row in queryset:
        date = str(row['date'])  # 将日期转换为字符串
        if date not in data:
            data[date] = []
        data[date].append({'name': row['subject'], 'value': row['Paper_Num'], 'date': date})


    data_list = list(data.values())

    # 将数据写入JavaScript文件

    from utils import querySetToJson
    res = querySetToJson(data_list)
    return HttpResponse(res, content_type='application/json')


def get_chart_data(request):
    chart_data = Papers.objects.values('word', 'frequency')
    return JsonResponse(list(chart_data), safe=False)

def relationdata(request):
    queryset = total.objects.values('date', 'Paper_Num', 'subject')

    data = {}
    for row in queryset:
        date = str(row['date'])  # 将日期转换为字符串
        if date not in data:
            data[date] = []
        data[date].append({'name': row['subject'], 'value': row['Paper_Num'], 'date': date})
    data_list = list(data.values())
    # 将数据写入JavaScript文件
    return JsonResponse(list(data_list), safe=False)

def Forecastdata(request):
    queryset = Forecast.objects.values('date', 'category', 'number')
    data = {}
    for row in queryset:
        date = str(row['date'])  # 将日期转换为字符串
        if date not in data:
            data[date] = []
        data[date].append({'date': date, 'category': row['category'], 'number': row['number']})

    data_list = list(data.values())
    from utils import querySetToJson
    res = querySetToJson(data_list)
    return HttpResponse(res, content_type='application/json')
