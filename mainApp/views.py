from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import *

def homePage(Request):
    csdata = CarouselSlider.objects.all()
    nadata = Product.objects.filter(category=1)
    trdata = Product.objects.filter(category=2)
    branddata = Brand.objects.all()
    subcdata = SubCategory.objects.all()
    return render(Request,"index.html",{"csdata":csdata,"nadata":nadata,"trdata":trdata,"branddata":branddata,"subcdata":subcdata})

def newsletterSubscription(Request):
    if(Request.method=="POST"):
        n = NewsletterSubscription()
        n.email = Request.POST.get("email")
        if(NewsletterSubscription.objects.filter(email=n.email)):
            messages.error(Request,"Already Subscribed by this Email!!!")
        else:
            n.save()
            messages.success(Request,"Subscribed Successfully!!!")
    return redirect("/")

def aboutPage(Request):
    return render(Request,"about.html")

def shopPage(Request,ct,mc,sc,br):
    if(ct=="All" and mc=="All" and sc=="All" and br=="All"):
        data = Product.objects.all().order_by("id").reverse()
    elif(ct!="All" and mc=="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct)).order_by("id").reverse()
    elif(ct=="All" and mc!="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(maincategory=MainCategory.objects.get(name=mc)).order_by("id").reverse()
    elif(ct=="All" and mc=="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(subcategory=SubCategory.objects.get(name=sc)).order_by("id").reverse()
    elif(ct=="All" and mc=="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct!="All" and mc!="All" and sc=="All" and br=="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),maincategory=MainCategory.objects.get(name=mc)).order_by("id").reverse()
    elif(ct!="All" and mc=="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),subcategory=SubCategory.objects.get(name=sc)).order_by("id").reverse()
    elif(ct!="All" and mc=="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct=="All" and mc!="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(maincategory=MainCategory.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc)).order_by("id").reverse()
    elif(ct=="All" and mc!="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(maincategory=MainCategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct=="All" and mc=="All" and sc!="All" and br!="All"):
        data = Product.objects.filter(subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct=="All" and mc=="All" and sc!="All" and br!="All"):
        data = Product.objects.filter(subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct!="All" and mc!="All" and sc!="All" and br=="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),maincategory=MainCategory.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc)).order_by("id").reverse()
    elif(ct!="All" and mc!="All" and sc=="All" and br!="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),maincategory=MainCategory.objects.get(name=mc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct=="All" and mc!="All" and sc!="All" and br!="All"):
        data = Product.objects.filter(maincategory=MainCategory.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    elif(ct!="All" and mc!="All" and sc!="All" and br!="All"):
        data = Product.objects.filter(category=Category.objects.get(name=ct),maincategory=MainCategory.objects.get(name=mc),subcategory=SubCategory.objects.get(name=sc),brand=Brand.objects.get(name=br)).order_by("id").reverse()
    category = Category.objects.all()
    maincategory = MainCategory.objects.all()
    subcategory = SubCategory.objects.all()
    brand = Brand.objects.all()
    return render(Request,"shop.html",{"data":data,"category":category,"maincategory":maincategory,"subcategory":subcategory,"brand":brand,"ct":ct,"mc":mc,"sc":sc,"br":br})

def shopSingle(Request,id):
    sdata = Product.objects.get(id=id)
    return render(Request,"shop-single.html",{"sdata":sdata})

def loginPage(Request):
    if(Request.method=="POST"):
        username = Request.POST.get("username")
        password = Request.POST.get("password")
        user = authenticate(username=username,password=password)
        if(user is not None):
            login(Request,user)
            if(user.is_superuser):
                return redirect("/admin/")
            else:
                return redirect("/profile/")
        messages.error(Request,"Invalid Username or Password!!!")
    return render(Request,"login.html")

def logoutAPI(Request):
    logout(Request)
    return redirect("/login/")

def registerPage(Request):
    if(Request.method=="POST"):
        p = Request.POST.get("password")
        cp = Request.POST.get("cpassword")
        if(p==cp):
            b = Buyer()
            b.name = Request.POST.get("name")
            b.username = Request.POST.get("username")
            b.email = Request.POST.get("email")
            b.phone = Request.POST.get("phone")
            user = User(username=b.username,email=b.email)
            if(user):
                user.set_password(p)
                user.save()
                b.save()
                # messages.error(Request,"You Registered Successfully!!!")
                return redirect("/login/")
            else:
                messages.error(Request,"User Name Already Taken!!!")
        else:
            messages.error(Request,"Password and Confirm Password Doesn't matched!!!")
            
    return render(Request,"register.html")

@login_required(login_url="/login/")
def profilePage(Request):
    user = User.objects.get(username=Request.user)
    if(user.is_superuser):
        return redirect("/login/")
    else:
        buyer = Buyer.objects.get(username=user.username)
        wishlist = Wishlist.objects.filter(user=buyer)
        orders = Checkout.objects.filter(user=buyer)
        if(Request.method=="POST"):
            buyer.name = Request.POST.get("name")
            buyer.email = Request.POST.get("email")
            buyer.phone = Request.POST.get("phone")
            buyer.addressline1 = Request.POST.get("addressline1")
            buyer.addressline2 = Request.POST.get("addressline2")
            buyer.addressline3 = Request.POST.get("addressline3")
            buyer.pin = Request.POST.get("pin")
            buyer.city = Request.POST.get("city")
            buyer.state = Request.POST.get("state")
            if(Request.FILES.get("pic")):   
                buyer.pic = Request.FILES.get("pic")
            buyer.save()
            return redirect("/profile/")
    return render(Request,"profile.html",{"user":buyer,"wishlist":wishlist,"orders":orders})

# def updateProfilePage(Request):
#     return render(Request,"update-profile.html")

@login_required(login_url="/login/")
def addToCart(Request,id):
    cart = Request.session.get("cart",None)
    p = Product.objects.get(id=id)
    if(cart is None):
        cart = {str(p.id):{"pid":p.id,"pic":p.pic1.url,"name":p.name,"color":p.color,"size":p.size,"price":p.finalprice,"qty":1,"total":p.finalprice,"category":p.category.name,"maincategory":p.maincategory.name,"subcategory":p.subcategory.name,"brand":p.brand.name}}
    else:
        if(str(p.id) in cart):
            item = cart[str(p.id)]
            item["qty"] = item["qty"]+1
            item["total"] = item["total"]+item["price"]
            cart[str(p.id)] = item
        else:
            cart.setdefault(str(p.id),{"pid":p.id,"pic":p.pic1.url,"name":p.name,"color":p.color,"size":p.size,"price":p.finalprice,"qty":1,"total":p.finalprice,"category":p.category.name,"maincategory":p.maincategory.name,"subcategory":p.subcategory.name,"brand":p.brand.name})
    Request.session["cart"]=cart
    Request.session.set_expiry(60*60*24*60)
    return redirect("/shop-cart/")

@login_required(login_url="/login/")
def shopCart(Request):
    cart = Request.session.get("cart",None)
    c = []
    total = 0
    shipping = 0
    if(cart is not None):
        for value in cart.values():
            total = total + value["total"]
            c.append(value)
        if(total<1000 and total>0):
            shipping = 150
    final = total + shipping
    return render(Request,"shop-cart.html",{"cart":c,"total":total,"shipping":shipping,"final":final})

@login_required(login_url="/login/")
def deleteCart(Request,pid):
    cart = Request.session.get("cart",None)
    if(cart):
        for key in cart.keys():
            if(str(pid)==key):
                del cart[key]
                break
        Request.session["cart"] = cart
    return redirect("/shop-cart/")

@login_required(login_url="/login/")
def updateCart(Request,pid,op):
    cart = Request.session.get("cart",None)
    if(cart):
        for key,value in cart.items():
            if(str(pid)==key):
                if(op=="inc"):
                    value['qty'] = value['qty']+1
                    value["total"] = value["total"] + value["price"]
                elif(op=="dec" and value["qty"]>1):
                    value['qty'] = value['qty']-1
                    value["total"] = value["total"] - value["price"]
                cart[key] = value
                break
        Request.session["cart"] = cart
    return redirect("/shop-cart/")

@login_required(login_url="/login/")
def addToWishlist(Request,pid):
    try:
        user = Buyer.objects.get(username=Request.user.username)
        p = Product.objects.get(id=pid)
        try:
            w = Wishlist.objects.get(user=user,product=p)
        except:
            w = Wishlist()
            w.user = user
            w.product = p
            w.save()
        return redirect("/profile")
    except:
        return redirect("/admin")
    
@login_required(login_url="/login/")
def deleteWishlist(Request,pid):
    try:
        user = Buyer.objects.get(username=Request.user.username)
        p = Product.objects.get(id=pid)
        try:
            w = Wishlist.objects.get(user=user,product=p)
            w.delete()
        except:
            pass
    except:
        pass
    return redirect("/profile")
    
@login_required(login_url="/login/")
def shopCheckout(Request):
    try:
        buyer = Buyer.objects.get(username=Request.user)
        cart = Request.session.get("cart",None)
        c = []
        total = 0
        shipping = 0
        if(cart is not None):
            for value in cart.values():
                total = total + value["total"]
                c.append(value)
            if(total<1000 and total>0):
                shipping = 150
        final = total + shipping
        return render(Request,"shop-checkout.html",{"user":buyer,"cart":c,"total":total,"shipping":shipping,"final":final})
    except:
        return redirect("/admin")
    
@login_required(login_url="/login/")
def orderPage(Request):
    if(Request.method=="POST"):
        mode = Request.POST.get("mode")
        if(mode=="COD"):
            user = Buyer.objects.get(username=Request.user.username)
            cart = Request.session.get("cart",None)
            if(cart is None):
                return redirect("/cart")
            else:
                check = Checkout()
                check.user = user
                total = 0
                shipping = 0
                for value in cart.values():
                    total = total + value["total"]
                if(total<1000 and total>0):
                    shipping = 150
                final = total + shipping
                check.total = total
                check.shipping = shipping
                check.final = final
                check.save()
                for value in cart.values():
                    cp = CheckoutProducts()
                    cp.checkout = check
                    cp.p = Product.objects.get(id=value["pid"])
                    cp.qty = value["qty"]
                    cp.total = value["total"]
                    cp.save()
                return redirect("/confirmation")      
        else:
            pass
    else:
        return redirect("/shop-checkout")
    
@login_required(login_url="/login/")
def confirmationPage(Request):
    return render(Request,"confirmation.html")     
           
def blogPage(Request):
    return render(Request,"blog.html")

def contactPage(Request):
    if(Request.method=="POST"):
        cd = ContactDetail()
        cd.name = Request.POST.get("name")
        cd.phone = Request.POST.get("phone")
        cd.email = Request.POST.get("email")
        cd.subject = Request.POST.get("subject")
        cd.message = Request.POST.get("message")
        cd.save()
        messages.success(Request,"Form Submitted Successfully!!!") 
    return render(Request,"contact.html")