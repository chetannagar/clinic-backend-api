import factory
import random
from doctors.models import Doctor
from users.factories import UserFactory


class DoctorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Doctor

    user = factory.SubFactory(UserFactory, role='Doctor')  # Ensure the user is a doctor
    specialization = factory.Faker('job')
    experience = factory.LazyFunction(lambda: random.randint(1, 40))
    consultation_fee = factory.LazyFunction(lambda: round(random.uniform(50, 500), 2))

    @staticmethod
    def generate_weekly_schedule():
        # Sample weekly schedule with varying hours
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        schedule = {}
        for day in weekdays:
            start_hour = random.randint(8, 10)
            end_hour = random.randint(16, 18)
            schedule[day] = [{
                'start': f"{start_hour:02d}:00",
                'end': f"{end_hour:02d}:00"
            }]
        return schedule

    availability_schedule = factory.LazyFunction(generate_weekly_schedule)

    def __str__(self):
        return self.user.email