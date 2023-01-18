from django.db import models

# Create your models here.
class Book(models.Model):
    Title=models.CharField(max_length=80)
    Author=models.CharField(max_length=40)
    Isbn=models.CharField(max_length=20)
    Publisher=models.CharField(max_length=50)

    class Meta:
        db_table='book'
    
    def __str__(self)->str:
        return self.Title

