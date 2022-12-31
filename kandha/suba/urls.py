
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collectionsview,name='collections'),
    path('collections/<str:cname>/<str:pname>',views.service_details,name='service_details'),
    path('cart',views.cart_page,name='cart'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('about',views.about,name='about'),
    path('exterior',views.exterior,name='exterior'),
    path('interior',views.interior,name='interior'),
    path('WheelAligment',views.WheelAligment,name='WheelAligment'),
    path('WaterWash',views.WaterWash,name='WaterWash'),
    path('Enginework',views.Enginework,name='Enginework'),

]
