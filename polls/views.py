from django.shortcuts import render, HttpResponse
from .models import vote, voter
# Create your views here.
def Polls(request):
    if request.method == "POST":
        vid = request.POST.get('ID')
        result = voter.objects.get(voterId=vid)
        if result:
            if result.casted == 0:
                result.casted +=1
                result.save()
                return render(request, "polls/vote.html")
            else:
                return HttpResponse("You already casted vote")
        else:
            return HttpResponse("improper adhar card")
    return render(request, "polls/home.html")

def Cast(request):
    if request.method == "POST":
        cast = request.POST.get('votecas')
        can1 = 'liberals'
        can2 = 'conservative'
        can3 = 'ndp'
        can4 = 'green'
        can5 =  'bloc'
        result = vote.objects.get(id=1)
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
