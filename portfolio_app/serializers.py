from rest_framework import serializers

from portfolio_app.models import (
    Feature,
    Industry,
    KeyFeature,
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


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = ("name",)


class KeyFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyFeature
        fields = ("title", "description")
