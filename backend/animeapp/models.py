from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator 

# Create your models here.

class Anime(models.Model):
    STATUS_CHOICES = [
        ('viewed', 'Просмотрено'),
        ('want', 'Хочу посмотреть'),
    ]

    title = models.CharField(max_length=1000)
    stars = models.PositiveIntegerField(validators=[MaxValueValidator(10)])
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='want',
    )
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,related_name='animes')
    
    def __str__(self):
        return f"{self.title}|{self.stars}|{self.status}({self.id})"
