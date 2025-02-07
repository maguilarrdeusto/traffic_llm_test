import time
import requests
from django.conf import settings  # Permite acceder a la configuración de Django

# URL del servicio de optimización real
OPTIMIZATION_SERVICE_URL = getattr(settings, "OPTIMIZATION_SERVICE_URL", "http://external-service.com/optimize")

# Modo de optimización: 'test' (simulado) o 'real' (servicio externo)
OPTIMIZATION_MODE = getattr(settings, "OPTIMIZATION_MODE", "test")

def optimize_kpis(weights):
    """
    Lógica para optimizar los KPI en función del modo seleccionado.
    """
    if OPTIMIZATION_MODE == "test":
        return optimize_kpis_test(weights)
    else:
        return optimize_kpis_real(weights)

def optimize_kpis_test(weights):
    """
    Simulación de la optimización de KPI con normalización.
    """
    time.sleep(1)  # Simula un retraso en la optimización

    # Generamos valores arbitrarios para la simulación
    optimized_kpis = {
        "optimized_PublicTransport": weights["weight_PublicTransport"] * 1.1,
        "optimized_Congestion": weights["weight_Congestion"] * 0.9,
        "optimized_Emissions": weights["weight_Emissions"] * 0.8,
        "optimized_OperationalCost": weights["weight_OperationalCost"] * 1.2,
    }

    # Normalizar los KPI para que la suma sea 1.0
    total = sum(optimized_kpis.values())
    if total > 0:
        optimized_kpis = {key: value / total for key, value in optimized_kpis.items()}

    return optimized_kpis

def optimize_kpis_real(weights):
    """
    Llama al servicio de optimización real.
    """
    try:
        response = requests.post(OPTIMIZATION_SERVICE_URL, json={"weights": weights})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Error en la consulta al servicio de optimización: {e}"}

