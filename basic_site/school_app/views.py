from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def school(request):
    my_dir = {'insert_me':"Hello I am from views.py"}
    return render(request,'school.html',context=my_dir)
def academics(request):
    my_dir1={'insert_me':"Hello,I am from views.py"}
    return render(request,'academics.html',context=my_dir1)
def administration(request):
        my_dir2={'insert_me':"Hello,I am from views.py"}
        return render(request,'administration.html',context=my_dir2)
def campusfacilites(request):
    my_dir3={'insert_me':"Hello,I am from views.py"}
    return render(request,'campusfacilites.html',context=my_dir3)
def staff(request):
    my_dir4={'insert_me':"Hello,I am from views.py"}
    return render(request,'staff.html',context=my_dir4)
def about(request):
    my_dir5={'insert_me':"Hello,I am from views.py"}
    return render(request,'about.html',context=my_dir5)
