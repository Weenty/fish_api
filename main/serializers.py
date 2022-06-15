from pyexpat import model
from turtle import position
from rest_framework import serializers
from .models import *

class BoatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = '__all__'

class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    position = serializers.PrimaryKeyRelatedField(queryset = Positions.objects.all())
    class Meta:
        model = Person
        fields = '__all__'

class PlaceFishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceFishing
        fields = '__all__'

class BanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ban
        fields = '__all__'

class CatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catch
        fields = '__all__'

class FlightSerializerForGet(serializers.ModelSerializer):
    boat = BoatSerializer(read_only = True)
    crew = PersonSerializer(many=True, read_only=True)
    bans = BanSerializer(many=True, read_only=True)
    catch = CatchSerializer(many=True, read_only=True)
    class Meta:
        model = Flight
        fields = '__all__'

class FlightSerializerForPost(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class FlightHasPersonSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = FlightHasPerson
        fields = '__all__'

class FlightHasBanSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = FlightHasBan
        fields = '__all__'

class FlightHasCatchSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = FlightHasCatch
        fields = '__all__'