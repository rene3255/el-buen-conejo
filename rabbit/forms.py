from django import forms
from resources.models import Breed


class AddBreedForm(forms.ModelForm):
  
    breed = forms.ModelChoiceField(queryset=Breed.objects.all())
    sex = forms.ChoiceField(label="Sexo", choices=[('M', ('Macho')), ('H', ('Hembra'))])    
    rabbit_tag = forms.CharField(max_length=20)
    birth_date = forms.DateField()
    weight = forms.DecimalField(decimal_places=1,max_digits=3, min_digits=1)
    
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
                  'rabbits_number','is_public', 'cage_photo'
        ]
        exclude = ('farm',)
        
    