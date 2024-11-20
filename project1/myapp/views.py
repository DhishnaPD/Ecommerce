from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def print_hello(request):
    movie_data={
        'movies':[
        {
        'title':'GodFather',
        'year':1990,
        'summary':'It is a comedy movie',
        'success':'false'
        },
        {
        'title':'GoldFish',
        'year':1999,
        
        'success':'true'
        }

        ]}
    return render(request,'hello.html',movie_data)