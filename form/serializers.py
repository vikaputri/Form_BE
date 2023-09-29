from rest_framework import serializers
from .models import Form
from rest_framework.validators import UniqueValidator

class Formserializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ["name", "identification_number", "email", "date_of_birth"]