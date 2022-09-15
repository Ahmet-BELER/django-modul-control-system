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
               
     def  save(self, *args, **kwargs):
        self.slug=slugify(self.name)
        super().save(*args, **kwargs)           
       
   


class Blog (models.Model):
    title = models.CharField(max_length=200)
    #image = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True)
    #category= models.ForeignKey(Category ,null=True, default=5 ,on_delete= models.CASCADE)
    category= models.ManyToManyField(Category, blank=True)
    
    def __str__(self): 
        
        return f"{self.title}" 
    
    def  save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)
        
    
    
 