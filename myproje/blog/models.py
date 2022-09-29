from unicodedata import category
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import  RichTextField
# Create your models here.

class Category (models.Model):
     name=models.CharField(max_length=30)
     slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)

     
     def __str__(self):
            
        return f"{self.name}" 
     class Meta:
         db_table="categorys"
        
               
     def  save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)           
       
   


class User (models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    description = RichTextField()
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=True)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)
    #category= models.ForeignKey(Category ,null=True, default=5 ,on_delete= models.CASCADE)
    category= models.ManyToManyField(Category, blank=False)
    
    def __str__(self): 
        
        return f"{self.name}" 
    class Meta:
         db_table="users"
    
    def  save(self, *args, **kwargs):
        self.slug=slugify(self.email)
        super().save(*args, **kwargs)
        
    
    
 