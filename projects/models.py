from django.db import models

class OptimizationRequest(models.Model):
    id = models.BigAutoField(primary_key=True)  # Definir clave primaria explícita
    weights = models.JSONField()  # Pesos enviados a la API
    optimized_kpis = models.JSONField(null=True, blank=True)  # KPI optimizados recibidos
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"Request {self.id} - {self.created_at}"