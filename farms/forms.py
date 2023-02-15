from django import forms
from farms.models import ProducerProfile
from resources.models import City

class ProfileForm(forms.ModelForm):
  
    first_name = forms.CharField(label='Nombre(s)',
                 max_length=100,
                 widget=forms.TextInput(
                 attrs={'class': 'form-control'})
                )
    
    last_name  = forms.CharField(label='Apellido(s)',
                max_length=100, 
                )
    city      = forms.ModelChoiceField(queryset=City.objects.all())
    
       
    photo      = forms.ImageField()
    
    farm_name  = forms.CharField(label='Farm name', 
                max_length=150
                )
    
    address = forms.CharField(label='Domicilio', 
                              max_length=200)
    class Meta:
      
        model = ProducerProfile
        fields = ['first_name', 'last_name',
                  'city', 'photo', 'farm_name', 'address' 
        ]
   
    