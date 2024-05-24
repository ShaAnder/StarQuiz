from django.db import models

class Planet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='planets/')

    def __str__(self):
        return self.name
    

class Character(models.Model):
    name = models.CharField(max_length=100)
    planet = models.ForeignKey(Planet, related_name='characters', on_delete=models.CASCADE)
    bio = models.TextField()
    image = models.ImageField(upload_to='characters/')

    def __str__(self):
        return self.name
