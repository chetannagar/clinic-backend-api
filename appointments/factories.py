import datetime
import random
import uuid
import factory
from appointments.models import Appointment
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory


class AppointmentFactory(factory.django.DjangoModelFactory):
    """Factory for creating Appointment instances."""

    class Meta:
        """Meta class for AppointmentFactory."""

        model = Appointment

    id = factory.LazyFunction(uuid.uuid4)
    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    appointment_date = factory.Faker("future_date")
    appointment_time = factory.LazyFunction(
        lambda: datetime.time(
            hour=random.randint(8, 16), minute=random.choice([0, 15, 30, 45])
        )
    )
    status = factory.Iterator(
        [
            Appointment.STATUS_SCHEDULED,
            Appointment.STATUS_COMPLETED,
            Appointment.STATUS_CANCELED,
            Appointment.STATUS_RESCHEDULED,
        ]
    )
    reason = factory.Faker("sentence")
    notes = factory.Faker("text")
    # No need to define created_at and updated_at as they use auto_now_add and auto_now

    @factory.post_generation
    def notes_optional(self, create, extracted, **kwargs):
        """Make notes optional with a 30% chance of being null."""
        # This method is called after the instance is created
        # and allows for additional modifications.
        # If `extracted` is provided, it will override the default behavior
        # of the factory.
        # If `extracted` is None, we can set notes to None
        # with a 30% chance.
        if not create:
            return
        if random.random() < 0.3:  # 30% chance of notes being null
            self.notes = None
            self.save()
