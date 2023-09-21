from django.shortcuts import render
import pickle

def home(request):
    return render(request, 'index.html')

def getPredictions(url):
    model = pickle.load(open('phishing.sav', 'rb'))
    predict = [url]
    #predict = predict.append(url)

    prediction = model.predict(predict)
    
    if prediction == "bad":
        return 'bad'
    elif prediction == "good":
        return 'good'
    else:
        return 'error'

def result(request):
    url = str(request.GET['url'])

    result = getPredictions(url)
    return render(request, 'result.html', {'result': result})
