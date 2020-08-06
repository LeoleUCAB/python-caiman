from django import forms

SIZE_CHOICES= [
    ('personal', 'personal'),
    ('mediana', 'mediana'),
    ('familiar', 'familiar'),
    ]

INGREDIENT_CHOICES= [
    ('margarita', 'margarita'),
    ('peperoni', 'peperoni'),
    ('doble queso', 'doble queso'),
    ('jamon', 'jamon'),
    ('pimenton', 'pimenton'),
    ('aceitunas', 'aceitunas'),
    ('salchichon', 'salchichon'),
    ('champiñon', 'champiñon'),
    ]

class PizzaForm(forms.Form):
    your_size = forms.CharField(label='Que tamaño tendra su pizza?')
    your_ingredient = forms.CharField(label='Que ingrediente tendra su pizza?')