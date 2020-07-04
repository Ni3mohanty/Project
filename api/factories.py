import factory
import factory.django
import uuid
from faker import Faker
fake = Faker()
from .models import User, ActivityPeriod



class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    
    real_name = fake.name()
    tz = fake.timezone()


class ActivityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActivityPeriod

    user = factory.SubFactory(UserFactory)
    start_time = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")
    end_time = fake.date_time().strftime("%Y-%m-%d %H:%M:%S")



class UserWithActivityFactory(UserFactory):
    
    @factory.post_generation
    def activities(obj, create, extracted, **kwargs):
        
        if not create:
            
            return

        if extracted:
            for _ in range(extracted):
                ActivityFactory(user=obj)
        else:
            import random
            number_of_units = random.randint(1, 10)
            for n in range(number_of_units):
                ActivityFactory(user=obj)