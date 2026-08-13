from rest_framework import serializers

from portfolio_app.models import (
    Feature,
    Technology,
)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("name",)

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ("name",)