from django import forms
from resources.models import Breed, RabbitStatus
from rabbit.models import Rabbit
from cage.models import Cage
from farms.models import ProducerProfile
from django.core.exceptions import ValidationError


class AddRabbitForm(forms.ModelForm):
      
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)
        if request:
            self.fields['cage'].queryset = Cage.cages.cages_by_farm(request.user.id).all()
        
    breed = forms.ModelChoiceField(queryset=Breed.objects.all())
    sex = forms.ChoiceField(label="Sexo", 
                        choices=[('M', ('Macho')), 
                                 ('H', ('Hembra'))])    
    rabbit_tag = forms.CharField(max_length=30,initial="ebc-")
    birth_date = forms.DateField(required=False)
    rabbit_photo = forms.ImageField(required=False)
    rabbit_status = forms.ModelChoiceField(
                            queryset=RabbitStatus.objects.all()
                            )
    
    class Meta:
        model = Rabbit
        fields = ['breed', 'sex','rabbit_tag',
                  'birth_date',  
                  'rabbit_photo', 'rabbit_status',
                  'cage'
                 ]
        exclude = ('is_active','is_doe','is_buck')
        
        
    def clean_weight(self):
        value = self.cleaned_data['weight']
        return value
          
            
       
        
        
        
        
        