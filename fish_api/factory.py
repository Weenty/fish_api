from main.models import *
import factory
import datetime
import factory.fuzzy
from django.utils.timezone import now

class BoatFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Boat
    name = factory.Faker('sentence', nb_words=2)
    type = factory.Faker('sentence', nb_words=2)
    displacement = factory.Faker('pyint', min_value=0, max_value=10000)
    data_create = factory.LazyFunction(now)

class PositionsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Positions
    name = factory.Faker('sentence', nb_words=2)

class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person
    name = factory.Faker('name')
    addres = factory.Faker('address')
    position = factory.fuzzy.FuzzyChoice(Positions.objects.all())

class PlaceFishingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PlaceFishing
    name = factory.Faker('sentence', nb_words=2)
    discriptions = factory.Faker('sentence', nb_words=30)

class BanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ban
    exit_date = factory.LazyFunction(now)
    return_date = factory.LazyFunction(now)
    place = factory.fuzzy.FuzzyChoice(PlaceFishing.objects.all())
    quality = factory.fuzzy.FuzzyChoice(['Нормальна', 'Лучшее', 'Не очень', 'Хуже некуда'])

class CatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Catch
    name_fish = factory.Faker('sentence', nb_words=3)
    weight = factory.Faker('pyint', min_value=0, max_value=500)

class FlightFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Flight
    boat = factory.fuzzy.FuzzyChoice(Boat.objects.all())
    exit_date = factory.LazyFunction(now)
    return_date = factory.LazyFunction(now)

class FlightHasPersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FlightHasPerson
    flight = factory.fuzzy.FuzzyChoice(Flight.objects.all())
    person = factory.fuzzy.FuzzyChoice(Person.objects.all())

class FlightHasBanFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FlightHasBan
    flight = factory.fuzzy.FuzzyChoice(Flight.objects.all())
    ban = factory.fuzzy.FuzzyChoice(Ban.objects.all())

class FlightHasCatchFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = FlightHasCatch
    flight = factory.fuzzy.FuzzyChoice(Flight.objects.all())
    catch = factory.fuzzy.FuzzyChoice(Catch.objects.all())


