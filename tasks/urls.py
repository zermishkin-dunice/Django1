from django.urls import path
from . import views
from .views import AboutView

urlpatterns = [
    path('', AboutView.as_view(), name='task_list'),
]
