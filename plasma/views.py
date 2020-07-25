from django.shortcuts import render
#from . models import donar,recipient

# Create your views here.
def index(request):
    return render(request,'plasma/index.html')
def select(request):
    if request.method =="POST":
        if 'select' in request.POST:
            text=request.POST['select']
            if text=="all":
                x=People.objects.all()
                context = {
                    "x":x,
                }
                return render(request,"testapp/output.html",context)
            elif text=="on":
                x=People.objects.get(name__contains="on")
                context={
                    "x":x,
                }
                return render(request,"testapp/index.html",context)
            elif text=="number":
                x=People.objects.get(id=5)
                context={
                    "x":x,
                }
                return render(request,"testapp/index.html",context)
            elif text=="name":
                x=People.objects.get(name="steve")
                context={
                    "x":x
                }
                return render(request,"testapp/index.html",context)
            else :
                context={

                }
                return render(request,"testapp/drop.html",context)
        else:
            context={

            }
            return render(request,"testapp/drop.html",context)

    else:
        context={

        }
        return render(request,"testapp/drop.html",context)