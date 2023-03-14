from django import forms
from django.forms import DecimalField, TextInput
from diary.models import Diary
from django.core.exceptions import ValidationError
import datetime

class AddActivityForm(forms.ModelForm):
    activity_date = forms.DateField(initial=datetime.date.today)        
    activity = forms.CharField(
                widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
               )
    costs   = forms.DecimalField(
                      max_digits=10,
                      decimal_places=2,
                      widget=TextInput(attrs={'type':'number}'}),required=False
              )
    
    
    class Meta:
        model = Diary
        fields = ['activity_date', 'activity','costs']
        exclude = ('is_active','farm',)
        
        
          
            
       
        
        
        
        
        