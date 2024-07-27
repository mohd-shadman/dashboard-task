
from django.urls import path
from .views import dashboard_view,dashboard_data

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('dashboard-data/', dashboard_data, name='dashboard_data'),
]
