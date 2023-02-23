from django import forms
from resources.models import Breed, RabbitStatus
from resources.utils import RabbitsConst
from rabbit.models import Buck, Doe, Rabbit


class AddRabbitForm(forms.ModelForm):
  
    breed = forms.ModelChoiceField(queryset=Breed.objects.all())
    sex = forms.ChoiceField(label="Sexo", 
                        choices=[('M', ('Macho')), 
                                 ('H', ('Hembra'))])    
    rabbit_tag = forms.CharField(max_length=20)
    birth_date = forms.DateField(required=False)
    weight = forms.DecimalField(decimal_places=1,
                               max_digits=3, min_digits=1, 
                               required=False
              )
    father = forms.ChoiceField(queryset=Buck.objects.all())
    mother = forms.ChoiceField(queryset=Doe.objects.all())
    rabbit_photo = forms.ImageField()
    rabbit_status = forms.ChoiceField(
                            queryset=RabbitStatus.objects.all()
                            )
    observation = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Rabbit
        fields = ['breed', 'sex','rabbit_tag',
                  'birth_date', 'weight', 'father', 'mother',
                  'rabbit_photo', 'rabbit_status'
                 ]
        exclude = ('cage',)
        
    