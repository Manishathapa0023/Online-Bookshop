# feedback/urls.py
from django.urls import path
from . import views

app_name="feedback"
urlpatterns = [
    path('', views.feedback, name='feedback'),
    path('thank-you/', views.thank_you_feedback, name='thank_you_feedback'),
]
