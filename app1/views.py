from ast import Num
from email.headerregistry import Address
from platform import uname
from unicodedata import category
from click import confirm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from . models import *
from django.http import HttpResponse
from django.contrib import messages

from django.db.models.query_utils import Q

# Create your views here.

def hello(request):
    return HttpResponse("You are in school recruitment system................")

def SignupView(request):
    print("signup functions")
    if request.POST: 
        Name = request.POST['name']
        Email = request.POST['email']
        Number = request.POST['phonenumber']
        Address = request.POST['address']
        Password = request.POST['password']
        ConfirmPassword = request.POST['confirmPassword']
        Category = request.POST['cat']
        age = request.POST['age']
        location = request.POST['location']
        gender = request.POST['gender']
        print(len(Number))

        # if len(str(Number))>10 and len(str(Number))<10:
        #     print('inside number')
        #     # msg = "enter right phone number"
        #     return render(request, 'register.html', {'msg': 'enter right phone number'})


        
        try:
            data = signUp.objects.get(email=Email)
            if data:
                print(data)
                msg = "Email already registered"
                return render(request, 'register.html', {'msg': msg})
            
            elif ConfirmPassword == Password:
                print("pw matched")
                v = signUp()
                v.name = Name
                v.email = Email
                v.number = Number
                v.address = Address
                v.password = Password
                v.gender=gender
                v.location=location
                v.age=age

                if Category == 'rec':
                    Category = 0
                    v.isStu = Category
                else:
                    Category = 1
                    v.isStu = Category
                v.save()
                print(f"{v.name} Signed up successfully")
                return redirect('app1:LOGIN1')
            else:
                msg = 'Please Enter Same Password'
                return render(request , 'register.html',{'msg':msg}) 
        except:
            pass
         
    return render(request,'register.html')

def userLogin(request):
    if request.POST:
        print("insode post")
        em = request.POST.get('email')
        pass1 = request.POST.get('password')
      
        print("Inside first try block", em)
        check = signUp.objects.get(email = em)
        print("Email is ",em)
        if check.password == pass1:
            
            request.session['email'] = check.email

            print(f'{check.name} Successfully logged in')
            return redirect('app1:HOME')
        else:
            return HttpResponse('Invalid Password')
    return render(request,'login1.html')


def dashboard(request):
    if 'email' in request.session:
        name = signUp.objects.get(email = request.session['email'])
        
        student = name.isStu
        print(f"{name} is {student}")
        print(type(student))
        
        if request.POST: 
            # saving data in database
            data = studentData()
            data.name = request.POST['name']
            data.email = request.POST['email']
            data.city = request.POST['city']
            data.dob = request.POST['dob']
            data.uname = request.POST['uname']
            data.cname = request.POST['cname']
            data.pyear = request.POST['pyear']
            data.spi = request.POST['spi']
            data.pl = request.POST['pl']
            data.description = request.POST['description']
            data.save()
            print("Data Successfully Submitted")
            return HttpResponse("Data Successfully Submitted")
        
        details = studentData.objects.all()

        # search module start
        print("Inside search module")
        s = request.GET.get('search')
        print(s)
        if s:
            q = studentData.objects.filter(Q(name__icontains = s) | Q(email__icontains = s) | Q(city__icontains = s) | Q(dob__icontains = s) | Q(uname__icontains = s) | Q(cname__icontains = s) | Q(pyear__icontains = s) | Q(spi__icontains = s) | Q(pl__icontains = s) | Q(description__icontains = s))
        else:
            q = details
        print(q)
        return render(request,'dashboard.html', {'name': name, 'student': student, 'details': details, 's':q})
    return redirect('app1:LOGIN1')

def userLogOut(request):
    del request.session['email']
    print('User logged out successfully')
    return redirect('app1:LOGIN1')

def home(request):
    if 'email' in request.session:
        student1 = signUp.objects.get(email=request.session['email'])
        student = student1.isStu
        em = student1.email
        return render(request,'index3.html', {'student': student, 'em':em})
    return redirect('app1:LOGIN1')

def notFound(request):
    return render(request,'404.html')

def about(request):
    return render(request,'about-us.html')

def blogDetails(request):
    return render(request,'blog-detail.html')

def blogFull(request):
    return render(request,'blog-full-width.html')

def blogGrid(request):
    return render(request,'blog-grid.html')

def blog(request):
    return render(request,'blog.html')

def candidateDetails(request):
    if 'email' in request.session:
        key = ''
        if 'email' in request.session:
            
            if request.POST: 
                # saving data in database
                data = studentData()
                data.name = request.POST['name']
                data.email = request.POST['email']
                data.city = request.POST['city']
                data.dob = request.POST['dob']
                data.uname = request.POST['uname']
                data.cname = request.POST['cname']
                data.pyear = request.POST['pyear']
                data.spi = request.POST['spi']
                data.pl = request.POST['pl']
                data.description = request.POST['description']
                data.save()
                key = "Data Successfully Submitted"
                print(key)
            # search module start
            print("Inside search module")
            return render(request,'candidate-detail.html', {'key': key})
        return redirect('app1:LOGIN')
    return redirect('app1:LOGIN1')


def candidateListing(request):
    return render(request,'candidate-listing.html')

def companyDetails(request):
    return render(request,'company-detail.html')

def contact(request):
    key = ''
    if request.method == 'POST':
        db = ContactForm(name = request.POST.get('name'), phone = request.POST.get('phone') ,email = request.POST.get('email'), details = request.POST.get('details'))
        db.save()
        key = "Your Message has been sent successfully"
    return render(request,'contact-us.html', {'key': key})

def dashboard1(request):
    return render(request,'dashboard1.html')

def editProfile(request):
    return render(request,'edit-profile.html')

def faqs(request):
    return render(request,'faqs.html')

def jobDetails(request):
    return render(request,'job-detail.html')

def jobListing(request):
    obj = studentData.objects.all()
    return render(request,'job-listing.html', {'obj': obj})


def packages(request):
    return render(request,'packages.html')

def postJob(request):
    return render(request,'post-job.html')

def register(request):
    return render(request,'register.html')

def typography(request):
    return render(request,'typography.html')


# only for backup
def index1(request):
    return render(request,'index.html')

def index2(request):
    return render(request,'index2.html')
