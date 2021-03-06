from unicodedata import name
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.homepage,name='homepage'), 
    path('loginpage',views.loginpage,name='loginpage'),
    path('user_login',views.user_login,name='user_login'),
    path('admin_welcome',views.admin_welcome,name='admin_welcome'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('load_addemployee',views.load_addemployee,name='load_addemployee'),
    path('add_employee',views.add_employee,name='add_employee'),
    path('show_employee',views.show_employee,name='show_employee'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('signup',views.signup,name='signup'),
    path('usercreate',views.usercreate,name='usercreate'),
    path('userhome',views.userhome,name='userhome'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('products_add',views.products_add,name='products_add'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('cate',views.cate,name='cate'),
    path('addcate',views.addcate,name='addcate'),
    path('deleted/<int:pk>',views.deleted,name='deleted'),
    path('editproduct/<int:pk>',views.editproduct,name='editproduct'),
    path('details/<int:pk>/<int:k>/',views.details,name='details'),
    path('viewcart/<int:pk>',views.viewcart,name='viewcart'),
    path('deletecart/<int:pk>',views.deletecart,name='deletecart'),
    path('profile/<int:pk>',views.myprofile,name='myprofile'),
    path('items',views.listcart,name='listcart'),
    path('cart/<int:pk>/<int:k>/',views.cartitem,name='cartitem'),
    path('viewusers',views.viewusers,name='viewusers'),
    path('deleteuser/<int:pk>',views.deleteuser,name='deleteuser'),
    path('items',views.listcart,name='listcart'),
    path('deleteitem/<int:pk>',views.deleteitem,name='deleteitem'),
    path('map',views.map,name='map'),
]