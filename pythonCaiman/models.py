from django.db import models

class Ingredient(models.Model):
    id = models.DecimalField(primary_key= True, max_digits= 2, decimal_places= 0)
    size_id = models.DecimalField(decimal_places= 0, max_digits= 2)
    name = models.CharField(max_length= 30)
    price = models.DecimalField(decimal_places= 0, max_digits= 4)

    class Meta:
        db_table = 'Ingredient'
        unique_together = (('id', 'size_id'),)

class Pedido(models.Model):
    id = models.DecimalField(primary_key= True, decimal_places= 0, max_digits= 2)
    fecha = models.DateField()

    class Meta:
        db_table = 'Pedido'

class Size(models.Model):
    id = models.DecimalField(primary_key= True, decimal_places= 0, max_digits= 2)
    name = models.CharField(max_length= 30, null= True)
    price = models.DecimalField(decimal_places= 0, max_digits= 4)

    class Meta:
        db_table = 'Size'

class Pizza(models.Model):
    id = models.DecimalField(primary_key= True, decimal_places= 0, max_digits= 2)
    pizzaId = models.DecimalField(decimal_places= 0, max_digits= 2)
    size_fk = models.ForeignKey('Size', models.DO_NOTHING, db_column='size_fk')
    ingredient_fk = models.ForeignKey('Ingredient', models.DO_NOTHING, db_column='ingredient_fk', null= True)
    pedido_fk = models.ForeignKey('Pedido', models.DO_NOTHING, db_column='pedido_fk')

    class Meta:
        db_table = 'Pizza'
