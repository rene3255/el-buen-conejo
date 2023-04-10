from django import forms
from mating.models import Mating
from doe.models import Doe
from buck.models import Buck
from django.core.exceptions import ValidationError


class AddMatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):   
        super().__init__(*args, **kwargs)
        self.fields['doe'] = forms.ModelChoiceField(queryset=Doe.objects.all())
        self.fields['buck'] = forms.ModelChoiceField(queryset=Buck.objects.all())
    
    observations = forms.CharField(
                widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
               )
    mating_date = forms.DateField(required=False)
    mating_succeeded = forms.ChoiceField(label="Monta exitosa", choices=[(True, ('Si')), (False, ('No'))])      
    class Meta:
        model = Mating
        fields = ['doe', 'buck',
                  'observations',
                  'mating_date',
                  'mating_succeeded']
        
        exclude = ('is_active','farm',)
        
        
          
            
       
