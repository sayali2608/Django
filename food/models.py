from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=2000, default="https://www.dirtyapronrecipes.com/wp-content/uploads/2015/10/food-placeholder.png")
# https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.simplyrecipes.com%2Fthmb%2FPb4_cwer3Dv-cAb297od2Qr_GCU%3D%2F1777x1333%2Fsmart%2Ffilters%3Ano_upscale()%2F__opt__aboutcom__coeus__resources__content_migration__simply_recipes__uploads__2019__09__easy-pepperoni-pizza-lead-3-8f256746d649404baa36a44d271329bc.jpg&imgrefurl=https%3A%2F%2Fwww.simplyrecipes.com%2Frecipes%2Fhomemade_pepperoni_pizza%2F&tbnid=aqngmxMM2y9DEM&vet=12ahUKEwjM383o8fT6AhUPrnIEHW2GDlkQMygBegUIARDyAQ..i&docid=Ck5z3mFwtc-sLM&w=1777&h=1333&q=pizza&ved=2ahUKEwjM383o8fT6AhUPrnIEHW2GDlkQMygBegUIARDyAQ
