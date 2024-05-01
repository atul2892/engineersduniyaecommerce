from django.contrib import admin
from django.urls import path
from mainApp import views
from django.conf.urls.static import static 
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('newsletter/', views.newsletterSubscription),
    path('about/', views.aboutPage),
    path('shop/<str:ct>/<str:mc>/<str:sc>/<str:br>/', views.shopPage),
    path('shop-single/<int:id>/', views.shopSingle),
    path('add-to-cart/<int:id>/', views.addToCart),
    path('shop-cart/', views.shopCart),
    path('delete-cart/<int:pid>/', views.deleteCart),
    path('update-cart/<int:pid>/<str:op>/', views.updateCart),
    path('add-to-wishlist/<int:pid>/', views.addToWishlist),
    path('delete-wishlist/<int:pid>/', views.deleteWishlist),
    path('shop-checkout/', views.shopCheckout),
    path('order/', views.orderPage),
    path('confirmation/', views.confirmationPage),
    path('login/', views.loginPage),
    path('logout/', views.logoutAPI),
    path('register/', views.registerPage),
    path('profile/', views.profilePage),
    # path('update-profile/', views.updateProfilePage),
    path('blog/', views.blogPage),
    path('contact/', views.contactPage),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
