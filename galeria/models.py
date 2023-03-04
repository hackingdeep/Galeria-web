from django.db import models
from django.contrib.auth.models import AbstractUser


class Userr(AbstractUser):
    biografia = models.TextField(null=True,default='Coloca tu biografia')
    pasion = models.CharField(max_length=50,null=True,default='Coloca tu pasion')
    avatar = models.ImageField(null=True,blank=True,default='avatar.svg')
   

class Categoria(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    usuario = models.ForeignKey(Userr,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nombre



class Foto(models.Model):
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Userr,on_delete=models.CASCADE)
    imagen = models.ImageField(null=False,blank=False)
    descripcion = models.TextField() 

    def __str__(self) -> str:
        return self.descripcion
    