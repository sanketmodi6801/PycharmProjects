from django.http import HttpResponse
from django.shortcuts import render

"""old code ,

 def name(request):
     return HttpResponse('''<h1>Hey welcome to the site</h1> <br> click on the text to enter site <br>
     <a href = "https://www.youtube.com" > youtube.com </a>''')
  
  def about(request):
     return HttpResponse("Hii")"""


# new code , here everything will come from index.html file by render function.


def index(request):
    return render(request, 'index.html')


def analyse(request):
    texts = request.GET.get('text', 'default')
    punctuations = '''  ~!@#$%^&*()_:";<>,'.?/|[]{} '''
    analysed = " "
    for char in texts:
        if char not in punctuations:
            analysed = analysed + char
    param = {'analysed_text': analysed}
    return render(request, 'analysed text.html', param)
    # return HttpResponse("hello ")


def func():
    return HttpResponse("hello this is function..!!")
