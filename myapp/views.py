from django.shortcuts import render
from django.http import HttpResponse, response

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')
    
def myform(request):
    return render(request,'myform.html')

def process(request):
    print("welcome")
    print(request.method)
    print(request.POST)
    a = int(request.POST['t1'])
    b = int(request.POST['t2'])
    c = a+b
    print(c)
    return render(request,'ans.html',{'sum':c})

def register(request):
    return render(request,'register.html')

def reg(request):
    fname = request.POST['fname']
    mname = request.POST['mname']
    lname = request.POST['lname']
    contact = int(request.POST['contact'])
    cname = request.POST['cname']
    department = request.POST['department']
    address = request.POST['address']
    gender = request.POST['gender']
    email = request.POST['email']
    uname = request.POST['uname']
    print(fname, mname,lname,contact,cname,department,address,gender,email,uname)
    return HttpResponse("You are registerd successfully !!!")