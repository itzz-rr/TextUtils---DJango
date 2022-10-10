# I created this file manually

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("This is about Rishi <br> Rishi is very much intrested in programmings")

def exercise1(request):
    return HttpResponse("<h1>Exercise 1</h1>"
                        "<br> <button><a href='https://www.google.com'>Google</button></a> "
                        "<br> <button><a href='https://www.facebook.com'>Facebook</button></a>"
                        "<br> <button><a href='https://www.github.com'>GitHub</button></a>"
                        "<br> <button><a href='https://www.codewithharry.com'>Code With Harry</button></a>")

def analyze(request):
    # Getting Text
    djtext = request.POST.get('text', 'default')
    analyzeVal = request.POST.get('analyze', 'default')

    # Remove Punctuation Function
    if analyzeVal == "removePunc":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # Capitalizing First Letter Function
    elif analyzeVal == "capiFirst":
        analyzed = djtext.capitalize()
        params = {'purpose': 'Capitalizing First letter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # Capitalizing All Letter Function
    elif analyzeVal == "capiAll":
        analyzed = djtext.upper
        params = {'purpose': 'Capitalizing All letter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    # Lowercase All Letter Function
    elif analyzeVal == "lowerAll":
        analyzed = djtext.lower
        params = {'purpose': 'Lower All letter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("<script>alert('Please select any option')</script>")