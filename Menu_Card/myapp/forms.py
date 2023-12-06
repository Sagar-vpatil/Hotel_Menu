from django import forms
from .models import MenuUpload

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuUpload
        fields = '__all__'
        labels = {
            'photo':'Dish Photo',
             'name' : 'Dish Name',
             'category' : 'Dish Category',
             'price' : 'Dish Price',
                  }
        widgets = {
           
            'name': forms.TextInput(attrs={'class':'form-control mb-2','placeholder':''}),
            'category': forms.TextInput(attrs={'class':'form-control mb-2','placeholder':''}),
            'price': forms.TextInput(attrs={'class':'form-control mb-3 mt-2','placeholder':''}),
        }
