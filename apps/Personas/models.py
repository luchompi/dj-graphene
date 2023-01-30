from django.db import models

# Create your models here.
class Cliente(models.Model):
  """Model definition for Cliente."""
  uid = models.CharField(max_length=50, primary_key=True)
  nombre = models.CharField(max_length=50)
  apellido = models.CharField(max_length=50)
  direccion = models.CharField(max_length=50)
  telefono = models.CharField(max_length=50)
  email = models.CharField(max_length=50)

  # TODO: Define fields here

  class Meta:
    """Meta definition for Cliente."""

    verbose_name = 'Cliente'
    verbose_name_plural = 'Clientes'

  def __str__(self):
    return '%s %s %s'%(self.uid, self.nombre, self.apellido)