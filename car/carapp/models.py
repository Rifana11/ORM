from django.db import models
from django.contrib import admin
class Car(models.Model):
    Brand_name=models.CharField(max_length=20)
    Price_rate=models.IntegerField()
    Engine_type=models.CharField(max_length=20)
    Car_color=models.CharField(max_length=20)
    Manufacture_year=models.IntegerField()

class CarAdmin(admin.ModelAdmin):
    list_display=["Brand_name","Price_rate","Engine_type","Car_color","Manufacture_year"]


