from django import forms
from rabbit.models import Rabbit
from doe.models import Doe
from django.core.exceptions import ValidationError


class AddDoeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['doe_rabbit'] = forms.ModelChoiceField(queryset=Rabbit.fetch_doe_rabbits)
        
    doe_name = forms.CharField(max_length=50)
    selection_date = forms.DateField(required=False)
          
    class Meta:
        model = Doe
        fields = ['doe_name', 'doe_rabbit', 'selection_date']
        exclude = ('is_active','farm')
        
        
          
            
       
        
        
        
        
        