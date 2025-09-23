# Ex02 Django ORM Web Application
# Date:23.09.2025c
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM

## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 10 books

# PROGRAM
```
admin.py

from django.contrib import admin
from .models import Car,CarAdmin
admin.site.register(Car,CarAdmin)

models.py

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



```


# OUTPUT
![alt text](<Screenshot 2025-09-23 112146.png>)

![alt text](<Screenshot 2025-09-23 113519.png>)


# RESULT
Thus the program for creating a database using ORM hass been executed successfully
