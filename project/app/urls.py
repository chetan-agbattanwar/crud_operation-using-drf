from django.urls import path
from .views import showView,deleteView,updateView,createView

urlpatterns = [
    path('sv/',showView),
    path('cv/',createView),
    path('uv/<int:pk>/',updateView),
    path('dv/<int:pk>/',deleteView)
]