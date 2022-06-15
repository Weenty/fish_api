from datetime import datetime
from .models import *
from . import serializers
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404
from json import loads
from django.http import JsonResponse

class BoatList(generics.ListCreateAPIView):
    queryset = Boat.objects.all()
    serializer_class = serializers.BoatSerializer

class BoatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Boat.objects.all()
    serializer_class = serializers.BoatSerializer

class PositionsList(generics.ListCreateAPIView):
    queryset = Positions.objects.all()
    serializer_class = serializers.PositionsSerializer

class PositionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Positions.objects.all()
    serializer_class = serializers.PositionsSerializer

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer

class CatchList(generics.ListCreateAPIView):
    queryset = Catch.objects.all()
    serializer_class = serializers.CatchSerializer

class CatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Catch.objects.all()
    serializer_class = serializers.CatchSerializer

class PlaceFishingList(generics.ListCreateAPIView):
    queryset = PlaceFishing.objects.all()
    serializer_class = serializers.PlaceFishingSerializer

class PlaceFishingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaceFishing.objects.all()
    serializer_class = serializers.PlaceFishingSerializer

class BanList(generics.ListCreateAPIView):
    queryset = Ban.objects.all()
    serializer_class = serializers.BanSerializer

class BanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ban.objects.all()
    serializer_class = serializers.BanSerializer

class FlightList(generics.ListCreateAPIView):
    """
        POST-запрос на создание.
        {
        "boat": 1, - id лодки
        "crew":[1,2,3, ...], - массив id персонала команды
        "bans": [1,2, ...], - массив id банок
        "catch": [1,2, ...], - массив id улова
        "exit_date": "2022-05-19T10:17:10.573Z",
        "return_date": "2022-05-19T10:17:10.573Z"
        }
    """
    queryset = Flight.objects.all()
    serializer_class = serializers.FlightSerializerForGet
    def create(self, request):
        try: 
            data = request.data
            crew = data['crew']
            bans = data['bans']
            catches = data['catch']
            serializer = serializers.FlightSerializerForPost(data = request.data)
            if serializer.is_valid(raise_exception=True):
                flight = serializer.save()
                for id_person in crew:
                    add_person = serializers.FlightHasPersonSeriliazer(data={"flight": flight.id, "person": id_person})
                    if add_person.is_valid(raise_exception=True):
                        add_person.save()
                for id_ban in bans:
                    add_ban = serializers.FlightHasBanSeriliazer(data={"flight": flight.id, "ban": id_ban})
                    if add_ban.is_valid(raise_exception=True):
                        add_ban.save()
                for id_catch in catches:
                    add_catch = serializers.FlightHasCatchSeriliazer(data={"flight": flight.id, "catch": id_catch})
                    if add_catch.is_valid(raise_exception=True):
                        add_catch.save()
                return Response({"detail": 'Added'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            if 'flight' in locals():
                flight.delete()
                FlightHasPerson.objects.filter(flight=flight.id).delete()
                FlightHasBan.objects.filter(flight=flight.id).delete()
                FlightHasCatch.objects.filter(flight=flight.id).delete()
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class FlightDetal(APIView):
    """
        В качестве аргумента передовать id лодки.
    """
    def get_flight(self, id):
        return get_list_or_404(Flight.objects.filter(boat = id))

    def get(self, request, pk):
        serializer = serializers.FlightSerializerForGet(self.get_flight(pk), many=True)
        return Response(serializer.data)

class DataSotrFish(APIView):
    # ДОДЕЛАТЬ ЭТА
    def post(self, request):
        from_date = request.data['from_date']
        to_date = request.data['to_date']
        type_fish = request.data['type_fish']
        
        fishes = Catch.objects.filter(name_fish = type_fish)
        list_both = []
        for fish in fishes:
            flightHasCatch = FlightHasCatch.objects.filter(catch = fish.id)
            if flightHasCatch.exists():
                for item in flightHasCatch:
                    if item.flight.exit_date <= datetime.strptime(from_date, '%Y-%m-%d %H:%M') and item.flight.return_date >= datetime.strptime(to_date, '%Y-%m-%d %H:%M'):
                        list_both.append(item.flight.both)
        return JsonResponse({'both': list_both})