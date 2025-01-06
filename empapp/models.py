from django.db import models
from webapp.models import Category

# Create your models here.
class FoodEditing(models.Model):
    fname = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fname