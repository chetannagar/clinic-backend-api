import uuid
from rest_framework import serializers
from users.models import User
from patients.models import Patient
from doctors.models import Doctor

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RegisterPatientSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=20)
    firebase_uid = serializers.CharField(max_length=255, required=False, allow_blank=True)
    date_of_birth = serializers.DateField()
    gender = serializers.ChoiceField(choices=Patient.GENDER_CHOICES)
    address = serializers.CharField(required=False, allow_blank=True)
    emergency_contact = serializers.CharField(max_length=20)

    def create(self, validated_data):
        firebase_uid = validated_data.pop("firebase_uid", None) or f"local-{uuid.uuid4()}"
        user = User.objects.create_user(
            email=validated_data["email"],
            role=User.ROLE_PATIENT,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            firebase_uid=firebase_uid,
        )
        Patient.objects.create(
            user=user,
            date_of_birth=validated_data["date_of_birth"],
            gender=validated_data["gender"],
            address=validated_data.get("address", ""),
            emergency_contact=validated_data["emergency_contact"],
        )
        return user


class RegisterDoctorSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    phone_number = serializers.CharField(max_length=20)
    firebase_uid = serializers.CharField(max_length=255, required=False, allow_blank=True)
    license_number = serializers.CharField(max_length=100)
    specialization = serializers.CharField(max_length=255)
    qualifications = serializers.CharField(required=False, allow_blank=True)
    experience = serializers.IntegerField(min_value=0)
    consultation_fee = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        firebase_uid = validated_data.pop("firebase_uid", None) or f"local-{uuid.uuid4()}"
        user = User.objects.create_user(
            email=validated_data["email"],
            role=User.ROLE_DOCTOR,
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            phone_number=validated_data["phone_number"],
            firebase_uid=firebase_uid,
        )
        Doctor.objects.create(
            user=user,
            license_number=validated_data["license_number"],
            specialization=validated_data["specialization"],
            qualifications=validated_data.get("qualifications", ""),
            experience=validated_data["experience"],
            consultation_fee=validated_data["consultation_fee"],
        )
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
