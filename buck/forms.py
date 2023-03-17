from django import forms
from rabbit.models import Rabbit
from buck.models import Buck
from django.core.exceptions import ValidationError


class AddBuckForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['buck_rabbit'] = forms.ModelChoiceField(queryset=Rabbit.fetch_buck_rabbits)
        
    buck_name = forms.CharField(max_length=50)
    selection_date = forms.DateField(required=False)
          
    class Meta:
        model = Buck
        fields = ['buck_name', 'buck_rabbit', 'selection_date']
        exclude = ('is_active',)
        
        
          
            
       
        
        
        
        
        