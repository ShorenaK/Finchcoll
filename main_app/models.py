from django.db import models

# Create your models here.
class Finchcoll(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    bio = models.TextField(max_length=500)
    verified_artist = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Location(models.Model):
     location_name= models.CharField(max_length=150)
     finchcall = models.ForeignKey(Finchcoll, on_delete=models.CASCADE, related_name="location")


     def __str__(self):
        return self.location_name

class Season(models.Model):
    season_name = models.CharField(max_length=150)
    seasons = models.ManyToManyField(Location)


    def __str__(self):
        return self.season_name