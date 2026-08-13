from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from portfolio_app.models import (
    Challenge,
    Detail,
    Feature,
    Impact,
    Industry,
    KeyFeature,
    Project,
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


class ProjectSerializer(serializers.ModelSerializer):
    industry = IndustrySerializer()
    technologies = TechnologySerializer(many=True)
    features = FeatureSerializer(many=True)
    details = DetailSerializer()
    snapshot = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "uuid",
            "name",
            "short_description",
            "long_description",
            "snapshot",
            "industry",
            "technologies",
            "features",
            "is_featured",
            "date_added",
            "details",
        )

    @extend_schema_field(serializers.URLField(allow_null=True))
    def get_snapshot(self, obj) -> str | None:
        if not obj.snapshot:
            return None

        return obj.snapshot.url
