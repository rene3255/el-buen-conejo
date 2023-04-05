from django import forms
from mating.models import Mating
from doe.models import Doe
from buck.models import Buck
from django.core.exceptions import ValidationError


class AddMatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['doe_name'] = forms.ModelChoiceField(queryset=Doe.fetch_doe_name)
        self.fields['buck_name'] = forms.ModelChoiceField(queryset=Buck.fetch_buck_name)
    comments = forms.CharField(
                widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
               )
    mating_date = forms.DateField(required=False)
          
    class Meta:
        model = Doe
        fields = ['doe_name', 'doe_rabbit', 'mating_date']
        exclude = ('is_active',)
        
        
          
            
       
