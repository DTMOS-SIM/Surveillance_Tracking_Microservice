from django.contrib.auth.models import User
from rest_framework import serializers
from surveillance_api.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('id', 'name', 'x_position', 'y_position', 'related_to', 'date_created', 'date_updated')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('id', 'from_person', 'to_person', 'angle_start', 'angle_end', 'date_created', 'date_updated')


class ReportSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = ('name', 'timestamp', 'frame_count', 'model_id')


