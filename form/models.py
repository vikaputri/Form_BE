from django.db import models
    
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    identification_number = models.CharField(max_length=12, unique=True)
    email = models.EmailField(max_length = 255, unique=True)
    date_of_birth = models.DateField()

    def __str__(self) :
        return self.name
