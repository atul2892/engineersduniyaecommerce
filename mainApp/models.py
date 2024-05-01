from django.db import models

class CarouselSlider(models.Model):
    id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to="uploads")
    title = models.CharField(max_length=1000)
    heading = models.CharField(max_length=500)
    paragraph = models.TextField()
    
    def __str__(self):
        return str(self.id)+" "+self.title


class NewsletterSubscription(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField()
    
    def __str__(self):
        return str(self.id)+" "+self.email
    
class ContactDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    subject = models.CharField(max_length=1000)
    message = models.TextField()
    
    def __str__(self):
        return str(self.id)+" "+self.name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    stock = models.CharField(max_length=20, default="In Stock", null=True, blank=True)
    description = models.TextField()
    baseprice = models.IntegerField(default=0, null=True,blank=True)
    discount = models.IntegerField(default=0)
    finalprice = models.IntegerField(default=0, null=True,blank=True)
    pic1 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic2 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic3 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    pic4 = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    
               
    def __str__(self):
        return self.name
    
    
class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    addressline1 = models.CharField(max_length=150)
    addressline2 = models.CharField(max_length=150)
    addressline3 = models.CharField(max_length=150)
    pin = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pic = models.ImageField(upload_to="uploads",default="",null=True,blank=True)
    otp = models.IntegerField(default=-222444)    

    def __str__(self):
        return str(self.id)+" "+self.username
    
class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.id)+" "+self.user.username+" "+self.product.name

status = ((0,"Order Placed"),(1,"Not Packed"),(2,"Packed"),(3,"Ready To Ship"),(4,"Shipped"),(5,"Out For Delivery"),(6,"Delivered"),(7,"Cancelled"))
payment = ((1,"Pending"),(2,"Done"))
mode = ((1,"COD"),(2,"Online Payment"))    
class Checkout(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    total = models.IntegerField()
    shipping = models.IntegerField()
    final = models.IntegerField()
    rppid = models.CharField(max_length=30,default="",blank=True,null=True)
    date = models.DateTimeField(auto_now=True)
    paymentmode = models.IntegerField(choices=mode,default=0)
    paymentstatus = models.IntegerField(choices=payment,default=0)
    orderstatus = models.IntegerField(choices=status,default=0)
    
    def __str__(self):
        return str(self.id)+" "+self.user.username
    
class CheckoutProducts(models.Model):
    id = models.AutoField(primary_key=True)
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    p = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    total = models.IntegerField()
    
    def __str__(self):
        return str(self.id)+" "+str(self.p.id)