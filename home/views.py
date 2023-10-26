from django.shortcuts import render
from django.http import HttpResponse



def home1(request):
    return render(request, "index.html")

def home2(request):
    employees = [
    {'name': 'Alice', 'age': 28},
    {'name': 'Bob', 'age': 35},
    {'name': 'Charlie', 'age': 42},
    {'name': 'David', 'age': 30},
    {'name': 'Eva', 'age': 25},
    {'name': 'Frank', 'age': 47},
    {'name': 'Grace', 'age': 33},
    {'name': 'Henry', 'age': 55},
    {'name': 'Ivy', 'age': 29},
    {'name': 'Jack', 'age': 40}
]
    
    return HttpResponse("HTTP Response")

import http.client


def my_api_view(request):
    conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")

    headers = {
    'X-RapidAPI-Key': "5e9985cba9msh45778915201d825p150b01jsn4db887a8cbcc",
    'X-RapidAPI-Host': "quotes15.p.rapidapi.com"
}

    conn.request("GET", "/quotes/random/", headers=headers)

    res = conn.getresponse()
    data = res.read().decode("utf-8")  # Decode the response data to a string

    return render(request, 'index.html', {'api_data': data})
