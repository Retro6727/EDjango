from django.forms import ModelForm
from webapp.models import Food

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['foodname', 'category', 'available', 'description','price', 'image']
        labels = {
            'foodname': 'Food Name',
            'category': 'Category',
            'available': 'Available',
            'description': 'Food Description',
            'price': 'Food Price',
            'image': 'Image',
        }