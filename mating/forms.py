from django import forms
from mating.models import Mating
from doe.models import Doe
from buck.models import Buck
from django.core.exceptions import ValidationError


class AddMatingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        request = kwargs.pop('request', None) 
        super().__init__(*args, **kwargs)
        self.fields['doe'] = forms.ModelChoiceField(queryset=Doe.objects.filter(farm=request.user.id))
        self.fields['buck'] = forms.ModelChoiceField(queryset=Buck.objects.filter(farm=request.user.id))
        
        
    observations = forms.CharField(
                widget=forms.Textarea(attrs={'rows': 3, 'cols': 40})
               )
    mating_date = forms.DateField(required=True)
    mating_succeeded = forms.ChoiceField(label="Monta exitosa", choices=[(True, ('Si')), (False, ('No'))])      
    class Meta:
        model = Mating
        fields = ['doe', 'buck',
                  'observations',
                  'mating_date',
                  'mating_succeeded']
        
        exclude = ('is_active','farm',)
        
    
       
