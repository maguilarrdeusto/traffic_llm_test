from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OptimizationRequest
from .serializers import OptimizationRequestSerializer
from .api import optimize_kpis  # Importa la función de optimización

class OptimizationAPIView(APIView):
    def post(self, request):
        try:
            weights = request.data.get("weights", {})

            if not weights:
                return Response({"error": "No se encontraron valores en 'weights'."}, status=status.HTTP_400_BAD_REQUEST)

            # Guardar la solicitud en la base de datos
            opt_request = OptimizationRequest.objects.create(weights=weights)

            # Llamar a la optimización (según `settings.OPTIMIZATION_MODE`)
            optimized_kpis = optimize_kpis(weights)

            if "error" in optimized_kpis:
                return Response({"status": "error", "message": optimized_kpis['error']}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Guardar los KPI optimizados en la base de datos
            opt_request.optimized_kpis = optimized_kpis
            opt_request.save()

            return Response({"status": "success", "optimized_kpis": optimized_kpis, "message": "Optimización completada con éxito."})

        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
