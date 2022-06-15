from django.urls import path
from .views import *
urlpatterns = [
    path('boats/', BoatList.as_view()),
    path('boats/<int:pk>/', BoatDetail.as_view()),
    path('person/', PersonList.as_view()),
    path('person/<int:pk>/', PersonDetail.as_view()),
    path('positions/', PositionsList.as_view()),
    path('positions/<int:pk>/', PositionsDetail.as_view()),
    path('catch/', CatchList.as_view()),
    path('catch/<int:pk>/', CatchDetail.as_view()),
    path('place_fishing/', PlaceFishingList.as_view()),
    path('place_fishing/<int:pk>/', PlaceFishingDetail.as_view()),
    path('ban/', BanList.as_view()),
    path('ban/<int:pk>/', BanDetail.as_view()),
    path('flight/', FlightList.as_view()),
    path('flight/<int:pk>/', FlightDetal.as_view()),
    path('datasotr/', DataSotrFish.as_view())
]
