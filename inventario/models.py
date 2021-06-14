from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Encargado(models.Model):
    CARRERA_CHOICES = [
        ('ETN', 'Electrónica'),
        ('MEC', 'Mecánica'),
        ('TEL', 'Telecomunicaciones'),
    ]
    nombre = models.CharField(max_length=200)
    carrera = models.CharField(max_length=3, choices=CARRERA_CHOICES, default='ETN')
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Item(models.Model):
    nombre = models.CharField(max_length=150)
    marca = models.CharField(max_length=150)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    encargado = models.ForeignKey(Encargado, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def is_available(self):
        return self.cantidad > 0

    def __str__(self):
        return f'{self.marca}:{self.nombre}'


class Prestamo(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.item}: {self.fecha_prestamo}'