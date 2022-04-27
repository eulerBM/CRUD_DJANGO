from django.db import models

# Create your models here.

SEXO_CHOICES = (

    ('m', 'Masculino'),
    ('f', 'Feminino'),
)

class Cliente(models.Model):
    mome = models.CharField(max_length=40)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome
    
