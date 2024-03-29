from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Good evening")


def cal(request):
    if request.method == "POST":
        num = int(request.POST.get("num"))
        print("num ",num)
        if num%2 == 0:
            res = "even num"
        else:
            res = "odd num"
        return render(request, "cal.html", {'msg':res})
    return render(request, "cal.html")

def factorial(request):
    if request.method == "POST":
        num = int(request.POST.get("num"))
        print("num = ",num)
        f=1
        original_num = num
        while num>0:
            f = f*num
            num = num-1
            msg = f"Factorial of {original_num} is {f}"
        return render(request, "fact.html", {'msg':msg})
    else:
        return render(request,"fact.html")

def add(request):
    if request.method == "POST":
        n1 = int(request.POST.get("num1"))
        print("n1= ",n1)
        n2 = int(request.POST.get("num2"))
        print("n2= ", n2)
        res = n1+n2
        msg = f"Add of {n1} & {n2} is {res}"
        return render(request, "add.html", {'msg':msg})
    else:
        return render(request, "add.html")