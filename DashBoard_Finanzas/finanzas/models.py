from django.db import models

class ConfiguracionUsuario(models.Model):
    ingresos_mensuales = models.DecimalField(decimal_places=2, max_digits=10)

    presupuesto_total = models.DecimalField(decimal_places=2, max_digits=10)

    fecha_inicio = models.DateTimeField()

    def __str__(self):
        return f"Configuración desde {self.fecha_inicio}"

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    color = models.CharField(max_length=20)

    icono = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Gasto(models.Model):
    importe = models.DecimalField(decimal_places=2, max_digits=10)

    fecha = models.DateTimeField()

    descripcion = models.CharField(max_length=100, blank= True)

    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="gastos")

    def __str__(self):
        return f"{self.categoria.nombre} - {self.importe}€"

class PresupuestoCategoria(models.Model):
    usuario = models.ForeignKey(
        ConfiguracionUsuario,on_delete=models.CASCADE, related_name="presupuestos")

    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name="presupuestos")

    porcentaje = models.PositiveIntegerField()

    limite = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return f"{self.categoria.nombre} - {self.porcentaje}%"



