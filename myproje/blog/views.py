from unicodedata import category
from django.shortcuts import (get_object_or_404,
                              redirect,
                              render,
                              HttpResponseRedirect)
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from blog.models import User, Category
from .forms import categoryForm ,userForm
from django.template import loader
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

 
 
 
def search (request):

    if request.method == "POST":
     name=request.POST["name"]
     users=User.objects.filter(name=name)
     
     
   
     return render(request,'search.html', {"users":users })
 
    else:
        return render(request,'search.html', {}) 
 
def create_user(request):
    context = dict()
    url = request.META.get('HTTP_REFERER')
    
    if request.method == 'POST':
            form =   userForm(request.POST)
            if form.is_valid():
               message=form.save(commit=False)
               message.save()
               return HttpResponseRedirect(url)
    else:
        context['form'] = userForm()  
    return render(request,'CreateUser.html', context)  

def create_category(request):
    
    context = dict()
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form =   categoryForm(request.POST)
        if form.is_valid():
            message=form.save(commit=False)
            message.save()
            return HttpResponseRedirect(url)
    else:
        context['form'] = categoryForm()  
    return render(request,'CreateCategory.html', context)    
           
def index(request):
    if not request.user.is_authenticated:
     return redirect("login")
    contex={
        "users": User.objects.filter(is_active=True , is_home=True),
        "categories":Category.objects.all()
    }
    
    return render(request, 'blog/index.html' ,contex)

def blogs(request):
    if not request.user.is_authenticated:
         return redirect("login")
    contex={
        "users": User.objects.filter(is_active=True),
        "categories":Category.objects.all()
    }
    return render(request, 'blog/blogs.html', contex)
   
def blog_details(request, slug):   
    users= User.objects.get(category__slug=slug)   
    return render(request,  'blog/blogs-detail.html' , {
        "users":users
    } )     
    
def blogs_by_category(request, slug):
  contex={
      "users":Category.objects.get(slug=slug).user_set.filter(is_active=True ),
        #"blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug,
        "User":User.objects.all(),
      
    }
  return render(request, 'blog/category_detail.html', contex)
    
def add_category(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        
        
        Category.objects.create(name=name,)
        return render(request,"add_category.html" , {"msg":"Category added successfully"})
        
    else:
        return render(request,"add_category.html" , {})
    

def update_category(request, slug):
    
    category = Category.objects.get(slug=slug)
    template = loader.get_template("update_category.html")
    


    context = {
      
      "category": category,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    name=request.POST['name']
    
    category= Category.objects.get(id=id)
    category.name=name
    category.save()
    return HttpResponseRedirect(reverse('home'))

def updaterecord_user (request,slug):
    name=request.POST['name']
    surname=request.POST['surname']
    email=request.POST['email']
    description=request.POST['description']
    category=request.POST['category']
    
    user= User.objects.get(slug=slug)
    user.name=name
    user.surname=surname
    user.email=email
    user.description=description
    user.category.set([category])

    user.save()
    return HttpResponseRedirect(reverse('home'))

def delete (request,id):
    category= Category.objects.get(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('home'))

def add_user(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        email=request.POST.get('email')
        description=request.POST.get('description')
      
        category_names = [x.name for x in Category.objects.all()]
        category_ids =[] 
        
        
        for x in category_names:
            if request.POST.get(x):
                category_ids.append(int(request.POST.get(x)))
            else:
               print("ahmet")     
                
        user = User.objects.create(name=name, 
                                   email=email,
                                   surname=surname,
                                   description=description,
                                  
                                   )        
        for x in category_ids:
            user.category.add(Category.objects.get(id=x))
        
        return render(request, "add_user.html" ,{"msg":"user added"})    

    else:
            return render(request, "add_user.html" ,{"category": Category.objects.all()}) 

def user_delete (request,slug):
    user = User.objects.get(slug=slug)
    user.delete()
    return HttpResponseRedirect(reverse('home'))  

def update_user(request,slug):
    category= Category.objects.all()
    user=User.objects.get(slug=slug)
    template = loader.get_template("update_user.html")
    
    context = {'user':user,
               'category':category}

    return HttpResponse(template.render(context, request))










    
''' def category_create(request):
        
    contex={}
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save() 
    
    contex['form']  =  form
    return render(request, "create_categor.html" ,contex)  '''      
    
  
  
  
  
  
  
  
  
  
  
  
  
     
    
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