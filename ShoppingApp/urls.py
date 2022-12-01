from django.urls import path
from ShoppingApp import views
app_name="ShoppingApp"

urlpatterns = [
    path('',views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/',views.allProdCat, name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.product, name='prodCatedetail'),
    path('login',views.login,name='login'),
    path('index',views.index,name='index'),
    # path('contact',views.contact,name='contact'),
    path('nav',views.nav,name='nav'),
    path('base',views.base,name='base')
    
]