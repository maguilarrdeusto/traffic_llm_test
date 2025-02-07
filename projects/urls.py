from django.urls import path
from .views import OptimizationAPIView

urlpatterns = [
    path('optimize/', OptimizationAPIView.as_view(), name='optimize'),
]