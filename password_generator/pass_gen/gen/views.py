from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
import random


def home(request):
    return render(request,'gen_p\home.html')
def password(request):
    key = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length',12))

    if length>15 or length<6:
        return render(request,'gen_p\err_home.html')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()~`-_=+[{}]\|;:?/'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    for x in range(length):
        key += random.choice(characters)

    return render(request,'gen_p\gen_pass.html',{'password':key})
