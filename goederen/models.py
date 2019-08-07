from django.db import models
from django.utils import timezone

# Create your models here.
class Goederen(models.Model):
    naam = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.naam


class GoederenNotitie(models.Model):
    goederen = models.ForeignKey(Goederen, related_name='notities', on_delete=models.CASCADE)
    notitie = models.CharField(max_length=255)



