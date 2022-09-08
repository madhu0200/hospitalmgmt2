from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import blogs,register_doctor
from .forms import *
# Create your views here.
usernames=[]
def home(request):
    return render(request,'home.html')


def registers(request):
    if request.method=='POST':

        #checking the entered username is avalilable or not
        user_name = request.POST.get('user_name')
        existed_user=register_doctor.objects.filter(user_name=user_name).first()

        #if entered username is not available
        if existed_user is not None:
            messages.warning(request,user_name+' user name is not available ! please try another ')
            return render(request,'register.html')

        #checking the password and confirm password are same
        password=request.POST.get('password')
        password2=request.POST.get('password2')

        if password !=password2:
            messages.warning(request,'passwords are not matching')
            return render(request,'register.html')


        form=doctors(request.POST,request.FILES)
        print(request.POST,request.FILES)
        if form.is_valid():
                form.save()
                messages.success(request,'registered successfully')
                return render(request, 'signin.html')
        else:
                messages.warning(request,'error occur')


    return render(request,'register.html')

def signin(request):
    if request.method=='POST':
        #cheking the user have account or not
        username = request.POST.get('user_name')
        # if len(usernames)!=0:
        #     for i in range(len(usernames)):
        #         del usernames[i]


        password=request.POST.get('password')
        auth=register_doctor.objects.filter(user_name=username,password=password).first()

        #authenticating the user

        if auth is not None:
            message=username+' logged in successfully'
            messages.success(request,message)
            return render(request,'dashboard.html',{'context':auth})
        else:
            message = username + ' enter details correctly !'
            messages.warning(request,message)
            return render(request,'signin.html')

    return render(request,'signin.html')
blogno=-1
def createblog(request,username):

    print(username)

    if request.method=='POST':
        user = request.POST.get('user_name')
        print('user')

        form=blogsform(request.POST,request.FILES)

        if form.is_valid():
            messages.success(request,'successfully uploaded')
            form.save()
        else:
            messages.warning(request,'error occured while uploading please try again !')
        global blogno

        if blogno is not None:
            blogs.objects.filter(id=blogno).delete()
        #print('username',usernames)
    return render(request,'createblogs.html',{'context':username})

def showblog(request,username):
    #print(usernames)
    users = register_doctor.objects.filter(user_name=username).first()
    #blog=blogs.objects.filter(user_name=usernames[0],draft=False)
    print(users)
    user_type=users.user_type
    print("usertype",user_type)
    if user_type=='patient':
        blog=blogs.objects.filter(draft='False')
        if len(blog)==0:
            return HttpResponse('there are no blogs present right now !')
        print(blog)
    else:
        blog = blogs.objects.filter(user_name=username,draft='False')
    # for b in blog:
    #     l=b.summary.split(' ')
    #     if len(l)>15:
    #         l=l[:15]
    #         l+="..."
    #     print(l)
    # print(len(blog))
    if len(blog) ==0 :
        return HttpResponse('there are no blogs made by you!')
    else:
        print(user_type)

        return render(request,'viewblog.html',{'context':blog,'username':username,'user_type':user_type})


def showdraft(request,username):
    #print(usernames)
    blog=blogs.objects.filter(user_name=username,draft='True').first()
    if blog is not None:
        global blogno
        blogno=blog.id
    else:
        return HttpResponse(username+'! there are no drafts saved buy you !')
    #print(blogno)
    return render(request,'createblogs.html',{'blog':blog,'context':username,'user_type':'doctor','draft':'True'})


from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter(name='split')
def split(value, key):
    """
        Returns the value turned into a list.
    """
    return value.split(key)