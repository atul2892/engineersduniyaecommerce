from django import template
from mainApp.models import Checkout,CheckoutProducts,Product
register = template.Library()

@register.filter(name="checkoutProducts")
def checkoutProducts(Request, checkoutid):
    checkout = Checkout.objects.get(id=checkoutid)
    cp = CheckoutProducts.objects.filter(checkout=checkout)
    c = []
    for item in cp:
        x = {"name":item.p.name,"maincategory":item.p.maincategory,"subcategory":item.p.subcategory,"brand":item.p.brand,"color":item.p.color,"size":item.p.size,"price":item.p.finalprice,"qty":item.qty,"total":item.total,"pic":item.p.pic1.url,}
    return cp
