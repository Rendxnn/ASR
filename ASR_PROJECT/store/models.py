from django.db import models

# Create your models here.

class Ladrillo(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=300)
	imagen = models.ImageField(upload_to='productos/imagenes_productos')
	precio = models.FloatField()

	def __str__(self):
		return self.nombre



