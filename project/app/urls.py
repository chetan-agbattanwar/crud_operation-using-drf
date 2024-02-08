from django.urls import path
from .views import showView,deleteView,updateView,createView #function based api_view
from .views import studentGetPostAPIView,studentPutDeleteAPIView # class based APIView

urlpatterns = [
    path('sv/',showView),
    path('cv/',createView),
    path('uv/<int:pk>/',updateView),
    path('dv/<int:pk>/',deleteView),
    path('api/',studentGetPostAPIView.as_view()),
    path('api/<int:pk>/',studentPutDeleteAPIView.as_view())
]