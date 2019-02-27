from django.shortcuts import render
from .models import winedata

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


# Create your views here.



def index(request):
    return render(request,'wine/index.html')
#
# def login(request):
#      return render(request,'sorting/login.html')
def asr(request):
    return render(request,'wine/asr.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('../login')
    else:
        form = UserCreationForm(request.POST)

    context = {'form':form}
    return render(request,'wine/register.html',context)



def home(request):
    q=winedata.objects.all()
    q=q[:3]
    return render(request,"wine/home.html",{'q':q})

def filter(request):
    q=winedata.objects.all()
    country=[]
    for i in q:
        country.append(i.country)
    country=list(set(country))
    country=['None']+country
    province=[]
    region_1=[]
    region_2=[]
    price=["None","Ascending","Descending"]
    variety=[]
    for i in q:
        province.append(i.province)
        region_1.append(i.region_1)
        region_2.append(i.region_2)
        variety.append(i.variety)


    province=list(set(province))
    region_1=list(set(province))
    region_2=list(set(province))
    variety=list(set(province))
    province=["None"]+province
    region_1=["None"]+region_1
    region_2=["None"]+region_2
    variety=["None"]+variety





    return render(request,"wine/filter.html",{"country":country,"province":province,"region_1":region_1,"region_2":region_2,"variety":variety,"price":price})


def logout(request):
    return render(request,"wine/logout.html")

def display(request):
    country=(request.POST["country"])
    price=(request.POST["price"])
    region_1=(request.POST["region_1"])
    region_2=(request.POST["region_1"])
    province=(request.POST["province"])
    variety=(request.POST["variety"])
    arr=list(winedata.objects.all())
    ans=[]

    kk=[]
    if(country!="None"):
        for i in arr:

            if(i.country==country):
                kk.append(i)
        arr=kk
        kk=[]
    if(region_1!="None"):
        for i in arr:
            if(i.region_1==region_1):
                kk.append(i)
        arr=kk
        kk=[]
    if(region_2!="None"):
        for i in arr:
            if(i.region_2==region_2):
                kk.append(i)
        arr=kk
        kk=[]
    if(province!="None"):
        for i in arr:
            if(i.province==province):
                kk.append(i)
        arr=kk
        kk=[]
    if(variety!="None"):
        for i in arr:
            if(i.variety==variety):
                kk.append(i)
    d={}
    for i in arr:
        if((i.price) in d):
            d[(i.price)].append(i)
        else:
            d[(i.price)]=[i]

    if(price!="None"):
        k=[]
        for i in sorted(d):
            k+=d[i]
        arr=k
        if(price!="Ascending"):
            arr=arr[::-1]












    return render(request,"wine/display.html",{"q":arr})
