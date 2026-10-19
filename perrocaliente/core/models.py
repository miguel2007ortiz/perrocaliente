from django.db import models

class Ficha(models.Model):
    grupo = models.CharField(max_length=15, unique=True) 
    nombre = models.CharField(max_length=55)  
    nivel = models.CharField(max_length=15)
    sede = models.CharField(max_length=55)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    def __str__(self):
        return f"Ficha {self.grupo} - {self.nombre}"

class Competencia(models.Model):
    codigo = models.CharField(max_length=15, unique=True)
    nombre = models.CharField(max_length=55)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

class Aprendiz(models.Model):
    documento = models.CharField(max_length=15)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(unique=True)
    celular = models.CharField(max_length=15) 
    ficha = models.ForeignKey("Ficha", on_delete=models.CASCADE, null=True, blank=True, related_name="aprendices")
    competencia = models.ManyToManyField("Competencia", blank=True, related_name="aprendices")
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.documento})"
