from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mysql
from . models import Card
from . models import achieve
from django.db.utils import IntegrityError

def home(req):
    rec=Card.objects.all().values()
    rec2=achieve.objects.all().values()
    return render(req,'index.html',{"rec":rec,"rec1":rec2})

def portfolio(req):
    return render(req,'portfolio.html')

def services(req):
    return render(req,'services.html')

def consultancy(req):
    return render(req,'consultancy.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def admin_login(req):
    return render(req,'admin_login.html')


def loginTask(req):
     email=req.POST.get('em1')
     password=req.POST.get('pa1')
     con=mysql.connect(host="localhost",user="root",password="root",database="python6",auth_plugin="mysql_native_password")
     cr=con.cursor()
     sql="select * from admin where email='{0}' and password='{1}' ".format(email,password)
     cr.execute(sql)
     rec=cr.fetchall()
     if rec==[]:
        return redirect("/admin_login")
     else:
        return redirect("/admin")

        
      
def admin(req):
     return render(req,'admin.html')

def addcard(req):
    return render(req,'addcard.html')

def card_input(req):
 try:
    ob=Card()
    ob.title=req.POST.get('ct')
    if len(req.FILES)!=0:
         ob.img=req.FILES['cimg']
    ob.data=req.POST.get('cd')
    ob.save()
    rec01="Card Added..."
    return render(req,'addcard.html',{'rec01':rec01})
 except:
    rec02="Something Went Wrong..."
    return render(req,'addcard.html',{'rec02':rec02})



# def addproduct(req):
#    if req.method=="GET": 
#       return render(req,"addpro.html")      
#    else:
#       ob=product()
#       ob.name=req.POST.get('name')
#       ob.size=req.POST.get('size')
#       if len(req.FILES)!=0:
#          ob.image=req.FILES['image']
#       ob.save()
#       return HttpResponse("done")



def showcard(req):
    rec=Card.objects.all().values()
    return render(req,'admin.html',{'rec':rec})


def achieve1(req):

    obj=achieve()
    if len(req.FILES)!=0:
         obj.img1=req.FILES['achieveimg']
    obj.data1=req.POST.get('achievedata')
    obj.save()
    rec01="Achieve Added..."
    return render(req,'addAchieve.html',{'rec01':rec01})
 
    # rec02="Something Went Wrong..."
    # return render(req,'addAchieve.html',{'rec02':rec02})


def showachieve(req):
    rec1=achieve.objects.all().values()
    return render(req,'index.html',{"rec1":rec1})


def addachieve(req):
    return render(req,'addAchieve.html')

def deletecard(req):
    id=int(req.GET.get('id'))
    ob=Card.objects.get(id=id)
    ob.delete()
    return redirect('/showcard')
    
def usercard(req):
    rec=Card.objects.all().values()
    return render(req,'index.html',{"rec":rec})

