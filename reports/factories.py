import factory
import random
from reports.models import MedicalReport, Prescription
from patients.factories import PatientFactory
from doctors.factories import DoctorFactory
from appointments.factories import AppointmentFactory

class MedicalReportFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicalReport

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    appointment = factory.LazyAttribute(lambda o: AppointmentFactory() if random.choice([True, False]) else None)
    report_type = factory.Faker('word')
    file_url = factory.Faker('url')
    diagnosis = factory.Faker('paragraph')
    prescription = factory.Faker('paragraph')

    # Optional: You could include a date for when the report was created
    # created_at = factory.LazyFunction(lambda: factory.Faker('date_this_year').generate({}))

class PrescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Prescription

    patient = factory.SubFactory(PatientFactory)
    doctor = factory.SubFactory(DoctorFactory)
    medications = factory.LazyFunction(lambda: [
        {'name': factory.Faker('word')(),
         'dosage': f"{random.randint(1, 5)}mg",
         'frequency': random.choice(['daily', 'twice daily', 'as needed'])}
        for _ in range(random.randint(1, 3))
    ])
    instructions = factory.Faker('sentence')

    # Optional: You could include a date for when the prescription was issued
    # issued_at = factory.LazyFunction(lambda: factory.Faker('date_this_year').generate({}))