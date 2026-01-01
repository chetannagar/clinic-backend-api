import datetime
import random
import uuid

import factory

from appointments.models import Appointment
from patients.factories import PatientFactory


class AppointmentFactory(factory.django.DjangoModelFactory):
    """Factory for creating Appointment instances."""

    class Meta:
        """Meta class for AppointmentFactory."""

        model = Appointment

    id = factory.LazyFunction(uuid.uuid4)
    patient = factory.SubFactory(PatientFactory)
    appointment_date = factory.Sequence(lambda n: datetime.date.today() + datetime.timedelta(days=n))
    appointment_time = factory.Sequence(
        lambda n: datetime.time(
            hour=9 + (n % 8), minute=random.choice([0, 15, 30, 45])
        )
    )
    status = factory.Iterator(
        [
            Appointment.STATUS_SCHEDULED,
            Appointment.STATUS_COMPLETED,
            Appointment.STATUS_CANCELED,
            Appointment.STATUS_RESCHEDULED,
            Appointment.STATUS_NO_SHOW,
        ]
    )
    reason = factory.Faker("sentence")
    notes = factory.Faker("text")
    
    @factory.lazy_attribute
    def doctor(self):
        # Reuse the doctor associated with the patient's user if available; otherwise create one.
        patient_doctor = getattr(self.patient.user, "doctor", None)
        if patient_doctor:
            return patient_doctor
        from doctors.factories import DoctorFactory  # Inline import to avoid circular dependency

        return DoctorFactory()

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
