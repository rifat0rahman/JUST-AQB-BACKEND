from rest_framework import serializers
from .models import CreatePdf

class CreatePdfSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatePdf
        fields = "__all__"