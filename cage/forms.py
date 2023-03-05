from django import forms
from cage.models import Cage


class AddCageForm(forms.ModelForm):
  
    cage_title = forms.CharField(label='Título de la jaula',
                 max_length=50,
                 widget=forms.TextInput(
                 attrs={'class': 'form-control'})
                )
    
    batch_number = forms.IntegerField(label='No. de Lote')
    #rabbits_number = forms.IntegerField(label='No. conejos')
    is_public = forms.ChoiceField(label="Jaula Pública o Privada", choices=[(True, ('Si')), (False, ('No'))])
    cage_photo = forms.ImageField(label="Upload")
    
    def clean_batch_number(self):
        number = self.cleaned_data['batch_number']
        
        if not number in range(1,12):
          raise forms.ValidationError("Número de lote erroneo")
        return number
      
    def clean_rabbits_number(self):
        rabbits_number = self.cleaned_data['rabbits_number']
        
        if not rabbits_number in range(1,12):
          raise forms.ValidationError("Número de lote erroneo")
        return rabbits_number
    
    class Meta:
      
        model = Cage
        fields = ['cage_title', 'batch_number', 
                  'is_public', 'cage_photo'
        ]
        exclude = ('farm', 'is_active','rabbits_number',)
        
    