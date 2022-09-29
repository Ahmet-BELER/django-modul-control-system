from mimetypes import init
from unicodedata import name
from django.urls import path 
from . import views 
from .forms import categoryForm,userForm
from blog.views import add_category,add_user,update_category,updaterecord,delete,update_user,user_delete,updaterecord_user,search
urlpatterns =[
    path ("", views.index , name="home"),
    path ("blogs", views.blogs, name="blogs"),
    path ("blogs/<slug:slug>" , views.blog_details, name="blog_details"),
    path ("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("Createcategory", views.create_category ,name="category_form"),
    path("Createuser", views.create_user ,name="user_form"),
    path('add-category/', add_category, name="add_category"),
    path('add-user/', add_user, name="add_user"),
    path('update_user/<slug:slug>', update_user, name="update_user"),
    path('update_user/updaterecord_user/<slug:slug>', updaterecord_user, name='updaterecord_user'),
    path('update_category/updaterecord/<int:id>', updaterecord, name='updaterecord'),
    path('delete/<int:id>', delete, name="delete"),
    path('user_delete/<slug:slug>', user_delete, name="user_delete"),
    path('update_category/<slug:slug>' ,update_category , name ="update_category"),
    path('search' , search, name="search"), 
    
   

] 



