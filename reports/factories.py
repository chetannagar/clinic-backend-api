import random

import factory
from faker import Faker

from appointments.factories import AppointmentFactory
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory
from reports.models import MedicalReport, Prescription

faker = Faker()

class MedicalReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicalReport

    appointment = factory.Maybe(
        factory.LazyFunction(lambda: random.choice([True, False])),
        yes_declaration=factory.SubFactory(AppointmentFactory),
        no_declaration=None,
    )
    patient = factory.LazyAttribute(lambda o: o.appointment.patient if o.appointment else PatientFactory())
    doctor = factory.LazyAttribute(lambda o: o.appointment.doctor if o.appointment else DoctorFactory())
    report_type = factory.Faker("word")
    file_url = factory.Faker("url")
    diagnosis = factory.Faker("paragraph")

class PrescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Prescription

    appointment = factory.Maybe(
        factory.LazyFunction(lambda: random.choice([True, False])),
        yes_declaration=factory.SubFactory(AppointmentFactory),
        no_declaration=None,
    )
    patient = factory.LazyAttribute(lambda o: o.appointment.patient if o.appointment else PatientFactory())
    doctor = factory.LazyAttribute(lambda o: o.appointment.doctor if o.appointment else DoctorFactory())
    medications = factory.LazyFunction(
        lambda: [
            {
                "name": faker.word(),
                "dosage": f"{random.randint(1, 5)}mg",
                "frequency": random.choice(["daily", "twice daily", "as needed"]),
            }
            for _ in range(random.randint(1, 3))
        ]
    )
    instructions = factory.Faker("sentence")