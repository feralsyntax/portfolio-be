from django.contrib import admin

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

admin.site.register(Detail)
admin.site.register(KeyFeature)
admin.site.register(Challenge)
admin.site.register(Impact)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "industry",
        "is_featured",
        "date_added",
    )

    list_filter = (
        "is_featured",
        "industry",
    )

    search_fields = (
        "name",
        "short_description",
        "long_description",
    )

    filter_horizontal = (
        "technologies",
        "features",
    )

    ordering = ("name",)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "date_added")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)
