from django.urls import path
from .import views

urlpatterns = [
    path('',views.HelloOrderview.as_view(),name='hello_order'),
]