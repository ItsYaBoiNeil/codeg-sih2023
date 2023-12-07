from django.shortcuts import render, HttpResponse
from .models import submittedURLs
import pickle

def getPredictions(url):
    model = pickle.load(open('phishing.pkl', 'rb'))
    predict = []
    predict = predict.append(url)
    prediction = model.predict(predict)    
    if prediction == 0:
        return 'no'
    elif prediction == 1:
        return 'yes'
    else:
        return 'error'

def home(request):
    return render(request,"home.html")

def model(request):
    return render(request,"model.html")

def URLs(request):
    items = submittedURLs.objects.all()
    return render(request,"urls.html", {"URLs":items})

def result(request):
    url = int(request.GET['url'])

    result = getPredictions(url)

    return render(request, 'result.html', {'result': result})