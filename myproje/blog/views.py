
from ast import Pass
from django.shortcuts import render,redirect
from blog.models import Blog, Category




# Create your views here.


def index(request):
    if not request.user.is_authenticated:
     return redirect("login")
    contex={
        "blogs": Blog.objects.filter(is_active=True , is_home=True),
        "categories":Category.objects.all()
    }
    
    return render(request, 'blog/index.html' ,contex)

def blogs(request):
    if not request.user.is_authenticated:
         return redirect("login")
    contex={
        "blogs": Blog.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, 'blog/blogs.html', contex)

   
def blog_details(request, slug):   
    blog= Blog.objects.get(slug=slug)   
    return render(request,  'blog/blogs-detail.html' , {
        "blog":blog
    } )     
    
def blogs_by_category(request, slug):
  contex={
      "blogs":Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        #"blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug
    }
  return render(request, 'blog/category_detail.html', contex)
    
    
      
    
     
    
'''     selectedBlog = None
    for blog in blogs:
        if blog["id"] == id: 
            selectedBlog = blog
    
     '''
'''          selectedBlog = [blog for blog in blogs if blog["id"]==id][0] '''



'''  contex={
        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories":Category.objects.all()
    }
    return render(request, 'blog/blogs.html', contex) ''' 