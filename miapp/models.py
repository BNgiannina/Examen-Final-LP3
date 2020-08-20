from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo=models.TextField()
    nombre=models.CharField(max_length=150)
    horas=models.TimeField(auto_now_add=True)
    creditos=models.IntegerField()
    estado=models.TextField()
