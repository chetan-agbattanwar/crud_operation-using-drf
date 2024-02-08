from django.urls import path
from .views import showView,deleteView,updateView,createView #function based api_view
from .views import studentGetPostAPIView,studentPutDeleteAPIView # class based APIView

#generic view
from .views import studentListAPIView,studentCreateAPIView,studentRetrieveAPIView,studentUpdateAPIView,studentDestroyAPIView
from .views import studentListCreateAPIView,studentRetrieveDestroyAPIView,studentRetrieveUpdateDestroyAPIView,studentRetrieveUpdateAPIView

urlpatterns = [
    path('sv/',showView),
    path('cv/',createView),
    path('uv/<int:pk>/',updateView),
    path('dv/<int:pk>/',deleteView),
    path('api/',studentGetPostAPIView.as_view()),
    path('api/<int:pk>/',studentPutDeleteAPIView.as_view()),

    #urls for generics
    path('l/',studentListAPIView.as_view()),
    path('c/',studentCreateAPIView.as_view()),
    path('lc/',studentListCreateAPIView.as_view()),
    path('r/<int:pk>/',studentRetrieveAPIView.as_view()),
    path('u/<int:pk>/',studentUpdateAPIView.as_view()),
    path('d/<int:pk>/',studentDestroyAPIView.as_view()),
    path('ru/<int:pk>/',studentRetrieveUpdateAPIView.as_view()),
    path('rd/<int:pk>/',studentRetrieveDestroyAPIView.as_view()),
    path('rud/<int:pk>/',studentRetrieveUpdateDestroyAPIView.as_view())
]