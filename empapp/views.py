from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from empapp.decorators import superuser_only
from empapp.forms import FoodForm
from webapp.models import Food
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_details')
@superuser_only
def dashboard1(request):
    products = Food.objects.all()
    total_amount_recieved = 0
    return render(request, "dashboard.html", {
        'products': products,
        'total_amount_recieved': total_amount_recieved
    })

def addfood(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Food Item is added successfully")
            return redirect('dashboard1')
    else:
        form = FoodForm()
    return render(request, 'addfood.html', {'form': form})

def update_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('dashboard1')
    else:
        form = FoodForm(instance=food)
    return render(request, 'editfood.html', {'form': form, 'food': food})

def delete_food(request, food_id):
    food = get_object_or_404(Food, id=food_id)
    food.delete()
    return redirect('dashboard1')

def delete_all_food(request):
    if request.method == 'POST':
        Food.objects.all().delete()  
        messages.success(request, "All food items have been deleted successfully.")
        return redirect('dashboard1')
    return redirect('dashboard1')