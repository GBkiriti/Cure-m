from django.shortcuts import render
from . models import donars,recipient

# Create your views here.
def index(request):
    return render(request,'plasma/index.html')
def select(request):
    if request.method =="POST":
        if 'select' in request.POST:
            text=request.POST['select']
            if text=="A-pos":
                x=donars.objects.get(blood="A+ve")
                context = {
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="A-neg":
                x=donars.objects.get(blood="A-ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="B-pos":
                x=donars.objects.get(blood="B+ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="B-neg":
                x=donars.objects.get(blood="B-ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="O-pos" :
                x=donars.objects.get(blood="O+ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="O-neg" :
                x=donars.objects.get(blood="O-ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="AB-pos" :
                x=donars.objects.get(blood="AB+ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
            elif text=="AB-neg" :
                x=donars.objects.get(blood="AB-ve")
                context={
                    "x":x,
                }
                return render(request,"plasma/display.html",context)
        else:
            context={

            }
            return render(request,"plasma/display.html",context)
    else:
        context={

        }
        return render(request,"plasma/display.html",context)