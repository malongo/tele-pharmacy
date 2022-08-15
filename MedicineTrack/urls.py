from django.urls import path
from . import views
import MedicineTrack

app_name="MedicineTrack"

urlpatterns = [
    path('', views.index, name='index'),
    path('shipping',views.shipping, name="shipping"),
    path('details',views.details, name="details")
]