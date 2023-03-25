
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login
from db.models.farmer import Farmer
from db.models.consumer import Consumer
def home(request):
    return render(request,"home.html",{})
      



def addPro(request):
    return render(request,"addProduct.html",{})


def userLog(request):
    return render(request,"login.html",{})

def farmerReg(request):
        if request.method=="POST":
            Fname = request.POST.get("Fname")
            Lname = request.POST.get("Lname")
            Mob = request.POST.get("Mob")
            Email = request.POST.get("Email")
            Pass1 = request.POST.get("Pass1")
            Pass2 = request.POST.get("Pass2")
            print(Fname,Lname,Mob,Email,Pass1,Pass2)
            f = Farmer()
            if f.objects.filter(email=Email).exist():
                messages.warning(request,"Email is already exist")
                return render(request,"login.html",{})
            else:
                f.fname = Fname
                f.lname = Lname
                f.femail = Email
                f.pass1 = Pass1
                f.pass2 = Pass2
                f.phone = Mob
                f.save()
                messages.success(request,"Your Account has been Successfully  created :-)")
                return redirect(request,"login.html")
        return render(request,"f_reg.html",{})

def farmerLog(request):
        if request.method=="POST":
            Email = request.POST.get("Email")
            Pass = request.POST.get("Pass")
            type = request.POST.get("type")
            print(Email,Pass,type)
            if type=="farmer":
                #user = authenticate(request,femail=Email,pass1=Pass)
                user = Farmer.getFarmerByEmail
                print("1")

                if user is not None:
                    print("2")
                    login(request,user)
                    return redirect("/")
                else:
                    print("3")

                    return render(request,"login.html",{})
        return render(request,"login.html")

@staticmethod
def getConsumerByEmail(email):
    return Consumer.objects.filter(cemail=email)



"""def isExist(self):
    if Consumer.objects.filter()"""
def userReg(request):
    if request.method=="POST":
        Fname = request.POST.get("Fname")
        Lname = request.POST.get("Lname")
        Email = request.POST.get("Email")
        Pass1 = request.POST.get("Pass1")
        Pass2 = request.POST.get("Pass2")
        Gender = request.POST.get("Gender")
        Phone = request.POST.get("Phone")
        Address = request.POST.get("Address")
        #return HttpResponse("<h1>Welcome to Home Page1</h1>")
        user = Consumer()
        user.fname = Fname
        user.lname = Lname
        user.cemail = Email
        user.pass1 = Pass1
        user.pass2 = Pass2
        user.phone = Phone
        user.address = Address
        if Gender=="male":
            user.gender = 'M'
        elif Gender=="female":
            user.gender = "F"
        else:
            user.gender = "O"
        user.save()
        messages.success(request,"Your Account has been Successfully  created :-)")
        print(Fname,Lname,Email,Pass1,Pass2,Phone,Gender,Address)
    return render(request,"user_reg.html",{})
    #return redirect("/user-registration")

