from django.db import models

# Create your models here.

class Country(models.Model):
    country_code = models.IntegerField(primary_key=True)
    country_name = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return str(self.country_code)
    
    
class Capital(models.Model):
    country_code = models.ForeignKey(Country, on_delete=models.CASCADE, unique=True)
    capital_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.capital_name