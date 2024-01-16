from django import forms 
from .models import Item

class ItemFom(forms.ModelForm):
    class Meta:
        model = Item 
        fields = ['item_name','item_desc','item_price','item_image','item_username']
