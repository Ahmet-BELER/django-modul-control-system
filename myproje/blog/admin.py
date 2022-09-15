from unicodedata import category
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home","slug", "selected_category")
    list_editable = ("is_active",)
    search_fields = ("title","description")
    list_filter = ("is_active","is_home","category")
    
    def selected_category(self , obj):
        html = "<ul>"
#
        for category in obj.category.all():
            html += "<li>" + category.name + "</li>"  
            
        html += "</ul>"    
        
        return mark_safe (html)
        
   
   
   
      
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,)

