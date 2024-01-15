from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default="https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_438,h_329,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/food-placeholder.jpg")
    
