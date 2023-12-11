from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .froms import Registeration,Train_form,User_form
from .models import Trains


# Create your views here.

def valid(request):
    if request.method=='POST':
        form=Registeration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('data not added')
    else:

        form=Registeration()
        return render(request,'register.html',{'form':form})
# @login_required(login_url='login')
def booking(request):
    if request.method=='POST':
        num=request.POST['train_number']
        destination=request.POST['train_destination']
        date=request.POST['date']
        var=Trains.objects.filter(train_number=num,train_destination=destination,date=date)
        return render(request,'trainlist.html',{'obj':var})
    else:
       form=Train_form()
       return render(request,'booking.html',{'form':form})
# @login_required(login_url='login')
def  Ticket(request,**args):
    if request.method=='POST':
        form=User_form(request.POST)
        if form.is_valid():
            var=request.POST['no_of_tickets']
            obj=Trains.objects.get(id=args['id'])
            if int(var)<=6:
                if(obj.no_of_tickets>0):
                    form.save()
                    obj.no_of_tickets=obj.no_of_tickets-int(var)
                    obj.save()
                    return HttpResponse('data added')
            else:
                    return HttpResponse('data not added')

    else:
        form=User_form()
        return render(request,'user.html',{'form':form})
