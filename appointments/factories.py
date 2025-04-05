import factory
import random
import datetime
from appointments.models import Appointment
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory

class AppointmentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Appointment

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    appointment_date = factory.Faker('future_date')
    appointment_time = factory.LazyFunction(
        lambda: datetime.time(hour=random.randint(8, 16), minute=random.choice([0, 15, 30, 45]))
    )
    status = factory.Iterator([
        Appointment.STATUS_SCHEDULED,
        Appointment.STATUS_COMPLETED,
        Appointment.STATUS_CANCELED,
        Appointment.STATUS_RESCHEDULED,
    ])
    reason = factory.Faker('sentence')
    notes = factory.Faker('text')

    @factory.post_generation
    def notes_optional(self, create, extracted, **kwargs):
        if not create:
            return
        if random.random() < 0.3:  # 30% chance of notes being null
            self.notes = None
            self.save()