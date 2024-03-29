from django import forms

from .models import Wish

class WishForm(forms.ModelForm):
    
    class Meta:
        model = Wish
        fields = ('title', 'description')