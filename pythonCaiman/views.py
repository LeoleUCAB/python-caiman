from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PizzaForm
from .models import *

# Create your views here.
def get_pizza(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PizzaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            size_name = form.cleaned_data['your_size']
            size = Size.objects.get(name = size_name)
            size_id = size.id
            pedido = Pedido.objects.latest('id')
            pedido_id = pedido.id + 1
            pizz = Pizza.objects.latest('id')
            pizz_id = Pizza.pizzaId + 1
            ingredient_name = form.cleaned_data['your_ingredient']
            if (ingredient_name != 'margarita'):
                ingredient = Ingredient.objects.get(name = ingredient_name)
                ingredient_id = ingredient.id
                pizza = Pizza(pizzaId=pizz_id, size_fk=size_id, ingredient_fk=ingredient_id, pedido_fk=pedido_id)
                pizza.save()
            else:
                pizza = Pizza(pizzaId=pizz_id, size_fk=size_id, pedido_fk=pedido_id)
                pizza.save()
            return HttpResponse("Registrado")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PizzaForm()

    return render(request, 'index.html', {'form': form})

def ready(request):
    return render(request, 'pizza.html')