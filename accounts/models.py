from django.db import models


class CoronaVirus(models.Model):
    district_name = models.CharField(max_length=200, null=True)
    total_cases = models.CharField(max_length=20, null=True)
    #new_cases = models.CharField(max_length=20, null=True)
    total_deaths = models.CharField(max_length=20, null=True)
    #new_deaths = models.CharField(max_length=20, null=True)
    total_recovered = models.CharField(max_length=20, null=True)
    #active_cases = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.district_name
