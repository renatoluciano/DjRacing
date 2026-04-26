from django.db import models

class RegistroDeVolta(models.Model):
    veiculo = models.CharField(max_length=50)
    tempo_segundos = models.FloatField()
    data_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.veiculo} - {self.tempo_segundos}s"
