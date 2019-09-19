from django.shortcuts import render, HttpResponse
from .models import vote, voter
# Create your views here.
def Polls(request):
   return render(request, "polls/home.html")

def Cast(request):
    if request.method == "POST":
        vid = request.POST.get('ID')
        can1 = 'liberals'
        can2 = 'conservative'
        can3 = 'ndp'
        can4 = 'green'
        can5 =  'bloc'
        result = vote.objects.get(id=1)
        result2 = voter.objects.get(voterId=vid)
        if result2.casted == 1:
            return HttpResponse("<h1>you already casted the vote</h1>")
        #Checking if vote is casted already.....
        if result2.casted == 0:
            result2.casted +=1
            result2.save()

        cast = request.POST.get('votecas')
        if cast == can1:
            result.liberals = result.liberals+1
            result.save()
            return HttpResponse(result.liberals)
        if cast == can2:
            result.conservative = result.conservative+1
            result.save()
            return HttpResponse(result.conservative)
        if cast == can3:
            result.ndp = result.ndp+1
            result.save()
            return HttpResponse(result.ndp)
        if cast == can4:
            result.green = result.green+1
            result.save()
            return HttpResponse(result.green)
        if cast == can5:
            result.bloc = result.bloc+1
            result.save()
            return HttpResponse(result.bloc)    

def Result(request):
    #if request.method == "POST":
        result = vote.objects.get(id=1)
        return render(request, "polls/result.html", {'result':result})
