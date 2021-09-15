from django.db import models

# Create your models here.
class Product(models.Model):  #Categoria produto
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=100.00)

    #Python3
    def __str__(self):
        return self.title

    #Python2
    def __unicode__(self):
        return self.title
