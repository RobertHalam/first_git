from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Welcome</h1>")


def redirect1(request):
    return HttpResponseRedirect("/app1")
    # or
    # return redirect('home')





def joker(request):
    return render(request,"joker.html")




