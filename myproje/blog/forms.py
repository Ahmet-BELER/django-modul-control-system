from pyexpat import model
from unicodedata import category
from django.forms import ModelForm,TextInput,forms,ModelMultipleChoiceField
from .models import Category , User

class categoryForm(ModelForm):
 class Meta:
    model = Category
    
    fields =["name"]
    
    widgets = {
            'name':TextInput(attrs={
                'class' : 'input'
            })
      }


class userForm(ModelForm):
    
    class Meta:
        model = User
        
        fields = ["name", "surname","email", "description", "category" ]
        
 
