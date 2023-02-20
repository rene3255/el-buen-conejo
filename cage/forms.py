from django import forms
from cage.models import Cage


class AddCageForm(forms.ModelForm):
  
    cage_title = forms.CharField(label='Título de la jaula',
                 max_length=50,
                 widget=forms.TextInput(
                 attrs={'class': 'form-control'})
                )
    
    batch_number = forms.IntegerField(label='No. de Lote')
    rabbits_number = forms.IntegerField(label='No. conejos')
    is_public = forms.ChoiceField(label="Jaula Pública o Privada", choices=[(True, ('Pública')), (False, ('Privada'))])
    cage_photo      = forms.ImageField(label="Upload")
    
    class Meta:
      
        model = Cage
        fields = ['cage_title', 'batch_number', 
                  'rabbits_number','is_public', 'cage_photo'
        ]
        exclude = ('farm',)
        
    