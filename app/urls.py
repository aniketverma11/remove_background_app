from django.urls import path
from .views import remove_bg

urlpatterns = [
    path('', remove_bg, name='remove_bg'),
    path('result/', remove_bg, name='remove_bg'),
]
