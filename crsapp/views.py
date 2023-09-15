from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CarForm
from .models import Registration, Car, Owner, Company
from django.db.models import Q

def indexpage(request):
    productlist = Car.objects.all()
    count = Car.objects.count()

    return render(request, "index.html", {"productlist": productlist, "count": count})

def userhome(request):
    if 'uname' in request.session:
        productlist = Car.objects.all()
        count = Car.objects.count()
        return render(request, "userhome.html", {'x':request.session['uname'] , "productlist": productlist, "count": count})

    else:
        return render(request, "session.html")

def contactpage(request):
    return render(request, "contactus.html")

def session(request):
    return render(request, "session.html")

def loginpage(request):
    return render(request, "login.html")

def userlogout(request):
    request.session.flush()
    return redirect("/")
def fl(request):
    h=request.session['email']
    return HttpResponse(h)

def owner(request):
    auname=request.session["uname"]
    return render(request,"owner.html",{"auname":auname})
def registration(request):
    name = request.POST['username']
    email = request.POST['emailAdress']
    contact = request.POST['phone']
    pwd = request.POST['password']
    r = Registration(reg_name=name, reg_email=email, reg_contactno=contact, reg_pwd=pwd)
    Registration.save(r)
    # subject = 'Welcome to my website!'
    # message = 'Thank you for registering on our website.'
    # from_email = 'amssdp@outlook.com'  # Replace with your email address
    # recipient_list = [email]
    # send_mail(subject, message, from_email, recipient_list)
    return render(request,"registersucess.html")
def checkuserlogin(request):
    emailid=request.POST["loginemail"]
    pwd=request.POST["loginPassword"]

    flag=Registration.objects.filter(Q(reg_email=emailid) & Q(reg_pwd=pwd))
    flag1=Company.objects.filter(Q(own_email=emailid)& Q(own_pwd=pwd))
    userscount = Registration.objects.count()
    userscount1 = Company.objects.count()
    if flag1:
        user = Company.objects.get(own_email=emailid)
        request.session["email"] = user.own_email
        request.session["uname"] = user.own_name
        emplist = Registration.objects.all()
        return render(request, "owner.html",{"uname": user.own_name,"emplist":emplist})
    elif emailid == "admin@gmail.com" and pwd == "admin":
        usersdata = Registration.objects.all()
        usersdata1 = Company.objects.all()
        return render(request, "adminpanel.html", {"users": usersdata,"count":userscount,"users1": usersdata1,"count1":userscount1})
    elif flag:
        user=Registration.objects.get(reg_email=emailid)
        request.session["email"] = user.reg_email
        request.session["uname"]=user.reg_name
        productlist = Car.objects.all()
        count = Car.objects.count()
        return render(request,"userhome.html",{"uname":user.reg_name,"productlist": productlist, "count": count})
    else:
        msg="Login Failed"
        return render(request,"loginfail.html",{"msg":msg})

def deleteuser(request,uid):
    Registration.objects.filter(id=uid).delete()
    return redirect("adminpanel")

def deleteowner(request,uid):
    Company.objects.filter(id=uid).delete()
    return redirect("adminpanel")

def empchangepwd(request):
    ename=request.session["uname"]
    return render(request,"changepwd.html",{"ename":ename})


def empupdatepwd(request):
    uname=request.session["uname"]

    opwd=request.POST["opwd"]
    npwd=request.POST["npwd"]

    flag = Registration.objects.filter(Q(reg_name=uname)&Q(reg_pwd=opwd))

    if flag:
        Registration.objects.filter(reg_name=uname).update(reg_pwd=npwd)
        msg = "Password Updated Successfully"
        return render(request, "changepwd.html", {"uname": uname,"msg":msg})
    else:
        msg = "Old Password is Incorrect"
        return render(request, "changepwd.html", {"uname": uname,"msg":msg})

def addproduct(request):
    auname = request.session["uname"]
    email=request.session["email"]

    form = CarForm()
    if request.method == "POST":
        formdata = CarForm(request.POST,request.FILES)
        if formdata.is_valid():
            formdata.save()
            msg="Car Added Successfully"
            return render(request, "addproduct.html", {"auname":auname,"productform": form,"msg":msg})
        else:
            msg = "Failed to Add Product"
            return render(request, "addproduct.html", {"auname":auname,"productform": form, "msg": msg})
    return render(request,"addproduct.html",{"auname":auname,"productform":form})

def viewcars(request):
    auname=request.session["auname"]
    render(request,"viewaproducts.html",{"auname":auname})

def viewaproducts(request):
    mail = request.session["email"]
    p=Company.objects.filter(own_email=mail)
    key=p[0].secure_key
    productlist = Car.objects.filter(secure_key=key)
    count = Car.objects.filter(secure_key=key).count()
    uname=request.session["uname"]
    return render(request,"viewaproducts.html",{"productlist":productlist,"count":count,"uname":uname})

def deleteproduct(request,uid):
    Car.objects.filter(id=uid).delete()
    return redirect("viewaproducts")

def adminpage(request):
    usersdata = Registration.objects.all()
    userscount = Registration.objects.count()
    return render(request, "adminpanel.html", {"users": usersdata,"count":userscount})

def rentpage(request):
    uname = request.session["uname"]
    return render(request, "rent.html", {"uname": uname})


def paysucc(request):
    uname = request.session["uname"]
    return render(request, "paymentsuccess.html",{"uname": uname})

