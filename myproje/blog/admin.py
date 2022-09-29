from unicodedata import category
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import User, Category

   
class contactCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
   
 
class contactUserAdmin(admin.ModelAdmin): 
    list_display = ('name',)


 
      
admin.site.register(User,contactUserAdmin)
admin.site.register(Category,contactCategoryAdmin)













''' 
class UserAdmin(admin.ModelAdmin):
      

    def selected_category(self , obj):
        html = "<ul>"
#
        for category in obj.category.all():
            html += "<li>" + category.name + "</li>"  
            
        html += "</ul>"    
        
        return mark_safe (html)
         '''