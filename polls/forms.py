from django.forms import ModelForm
from .models import vote

# Create the form class.
class votingForm(ModelForm):
     class Meta:
         model = vote
         fields = '__all__'