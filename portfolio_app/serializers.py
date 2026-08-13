from rest_framework import serializers

from portfolio_app.models import (
    Challenge,
    Detail,
    Feature,
    Impact,
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


class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = ("title", "description")


class ImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impact
        fields = ("title", "description")


class DetailSerializer(serializers.ModelSerializer):
    key_features = KeyFeatureSerializer(many=True)
    challenges = ChallengeSerializer(many=True)
    impacts = ImpactSerializer(many=True)

    class Meta:
        model = Detail
        fields = (
            "problem",
            "solution",
            "overview",
            "front_end_techs",
            "back_end_techs",
            "other_techs",
            "key_features",
            "challenges",
            "impacts",
            "live_site",
        )
