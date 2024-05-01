from django.contrib import admin
from .models import *

admin.site.register((CarouselSlider,NewsletterSubscription,ContactDetail,Category,MainCategory,SubCategory,Brand,Product,Buyer,Checkout,CheckoutProducts))