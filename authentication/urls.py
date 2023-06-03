from django.urls import path
from .import views

urlpatterns = [
    path('',views.HelloAuthview.as_view(),name='hello_auth'),
    path('signup/',views.UserCreateView.as_view(),name='sign_up')
]