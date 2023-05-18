# this is created by me..!!
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def addition(request):
    # num1 = request.GET.get('text', 'default')
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    VAL3 = val1+val2
    params = {'output': VAL3}
    return render(request, 'output.html', params)