from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth

from Apppetrol.models import cart, category, employee, fuel_price, product
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def loginpage(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

@login_required(login_url='loginpage')
def admin_welcome(request):
    return render(request,'welcome.html')

def addproduct(request):
    cors=category.objects.all()
    context={'cors':cors}
    return render(request,'addproduct.html',context)

def viewproduct(request):
    pro=product.objects.all()
    return render(request,'viewproduct.html',{'pro':pro})   

def cate(request):
    return render(request,'adcategory.html')

# def pryz(request):
#     return render(request,'addfuelprice.html')

def viewusers(request):
    std=User.objects.filter(is_superuser=0)
    return render(request,'admin-viewuser.html',{'std':std})

def deleteuser(request,pk):
    std=User.objects.get(id=pk) 
    std.delete()
    return redirect('viewusers')   

def user_login(request):
    if request.method=='POST':
        pro=product.objects.all()
        
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request,user)
                return redirect('admin_welcome')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome {username}')
                return render(request,'user-home.html',{'pro':pro, 'user':user})
                #return redirect('user_welcome')
        else:
            messages.info(request,"invalid username or password")
            return redirect('loginpage')
    return render(request,'home.html')

def products_add(request):
    if request.method=='POST':
        name=request.POST['product_name']
        descr=request.POST['description']
        price=request.POST['price']
        sel=request.POST['sel']
        cat=category.objects.get(id=sel)
        #image=request.FILES.get('file')
        if request.FILES.get('file')is not None:
            image = request.FILES.get('file')
        else:
            image = "static/image/default.jpg"

        pro=product(product_name=name,descrption=descr,price=price,image=image,category=cat)
        pro.save()
        messages.info(request,'product add suceessfully')
        return redirect('addproduct')
    return render(request,'addproduct.html')

def addcate(request):
    if request.method=='POST':
        name=request.POST['category_name'] 
        cat=category(category_name=name)
        cat.save()
        messages.info(request,'category add successfully') 
        return redirect('cate')
    return render(request,'adcategory.html') 

def editproduct(request,pk):
    pro=product.objects.get(id=pk)
    ca=cart.objects.all()
    if request.method=='POST':
        pro.product_name=request.POST['product_name']
        pro.descrption=request.POST['descrption'] 
        pro.price=request.POST['price']
        pro.image=request.FILES('file')  
        c=request.POST['sel']
        pro.category=category.objects.get(id=c) 
        pro.save()     
        return redirect('viewproduct')
    return render(request,'editproduct.html',{'pro':pro , 'ca':ca})

def deleted(request,pk):
    std=product.objects.get(id=pk)  
    std.delete()
    return redirect('viewproduct')  
   

@login_required(login_url='loginpage')
def admin_logout(request):
    auth.logout(request)
    return render(request,'home.html')

def load_addemployee(request):
    return render(request,'add_employee.html')

@login_required(login_url='loginpage')
def add_employee(request):
    if request.method=='POST':
        e_name=request.POST['ename']
        e_address=request.POST['eaddress']
        e_age=request.POST['eage']
        e_gender=request.POST['egender']
        e_mobile=request.POST['emobile']
        e_jdate=request.POST['dname']
        if request.FILES.get('photo') is not None:
            photo=request.FILES['photo']
        else:
            photo="static/images/default.png"
        emp=employee(emp_name=e_name,emp_address=e_address,emp_age=e_age,emp_gender=e_gender,emp_mobile=e_mobile,join_date=e_jdate,emp_photo=photo)
        emp.save()
        print('hi')
        return redirect('load_addemployee')
    return render(request,'add_employee.html')



@login_required(login_url='loginpage')
def show_employee(request):
    context=employee.objects.all()
    return render(request,'show_employee.html',{'dataread':context})

@login_required(login_url='loginpage')
def delete(request,pk):
    em=employee.objects.get(id=pk)
    em.delete()
    return redirect('show_employee')

def usercreate(request):
    if request.method=='POST':
        name=request.POST['first_name']
        lname=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username is already exists!!!...')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                     first_name=name,
                     last_name=lname,
                     username=username,
                     email=email,
                     password=password)
                user.save()
                messages.info(request,'successfully created')
        else:
             messages.info(request,'password does not match!!!....')   
             return redirect('signup') 
        return redirect('signup')                
    else:
        return render(request,'signup.html')

def userhome(request):
    pro=product.objects.all()
    return render(request,'user-home.html',{'pro':pro}) 

def viewcart(request,pk):
    ca=cart.objects.filter(User=pk) 
    return render(request,'cart.html',{'cart':ca})   

def deletecart(request,pk):
    ca=cart.objects.get(id=pk)
    ca.delete()
    #return redirect('viewcart')
    return render(request,'cart.html')

def myprofile(request,pk):
    std=User.objects.get(id=pk)
    return render(request,'profile.html',{'std':std})  

def listcart(request):
    ca=cart.objects.all()
    return render(request,'cartitems.html',{'item':ca})

def deleteitem(request,pk):
    item=cart.objects.get(id=pk)
    item.delete()
    return redirect('listcart')  

def cartitem(request,pk,k):
    prod=product(id=pk)
    user1=User(id=k)
    t=cart(product=prod,
          User=user1)
    t.save()
    return redirect('userhome')




def details(request,pk,k):
    pro=product.objects.get(id=pk)
    return render(request,'viewdetails.html',{'pro':pro, 'u':k})   

# def addfuel(request):
#     if request.method=='POST':
#         name=request.POST['fuel_price'] 
#         pry=category(fuel_price=name)
#         pry.save()
#         messages.info(request,'fuelprice add successfully') 
#         return redirect('pryz')
#     return render(request,'addfuelprice.html') 

def map(request):
    return render(request,'map.html')