from django.shortcuts import redirect, render
from app1.models import Branch
from app1.forms import Branchform
from app1.models import User
from app1.forms import Userform
from app1.models import Customermanager
from app1.forms import Customermanagerform
from app1.models import Book
from app1.forms import BookingForm
from app1.forms import Loginform


def homepage(request):
    if request.method == "POST":
        form = Loginform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('bb/')
            except Exception as e:
                print(e)
                pass
    else:
        form = Loginform()
    return render(request, 'login.html', {'form':form})

#
def branchmaster(request):
    if request.method == "POST":
        form = Branchform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('b/')
            except Exception as e:
                print(e)
                pass
    else:
        form = Branchform()
    return render(request, 'branchmaster.html', {'form':form})




def branchpage(request):
    branch = Branch.objects.all()
    return render(request, 'branch.html', {'branch': branch})


def edit(request,id):
    branch = Branch.objects.get(id=id)
    return render(request,'edit.html',{'branch':branch})

def update(request,id):
    branch = Branch.objects.get(id=id)
    form=Branchform(request.POST, instance=branch)
    try:
        form.save()
        return redirect('')
    except Exception as e:
        print(e)
        pass
    return render(request,'edit.html',{'branch':branch})


def locationmaster(request):
    if request.method == "POST":
        form = Userform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('ud/')
            except Exception as e:
                print(e)
                pass
    else:
        form = Userform()
    return render(request, 'locationmaster.html', {'form': form})


def userdetails(request):
    data = User.objects.all()
    return render(request, 'userdetails.html', {'data': data})


def customermanager(request):
    if request.method == "POST":
        form = Customermanagerform(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('c/')
            except Exception as e:
                print(e)
                pass
    else:
        form = Userform()
    return render(request, 'customermanager.html', {'form': form})


def customer(request):
    data = Customermanager.objects.all()
    return render(request, 'customer.html', {'data': data})


# def bookingmanager(request):
#     if request.method == "POST":
#         form = Bookingform(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('bo/')
#             except Exception as e:
#                 print(e)
#                 pass
#     else:
#         form = Bookingform()
#     return render(request, 'bookingmanager.html', {'form': form})


# def booking(request):
#     book = Book.objects.all()
#     return render(request, 'booking.html', {'book': book})

def bookingmanager(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('bo/')
            except Exception as e:
                print(e)
                pass
    else:
        form = BookingForm()
    return render(request, 'bookingmanager.html', {'form':form})


def booking(request):
    book = Book.objects.all()
    return render(request, 'booking.html', {'book':book})
