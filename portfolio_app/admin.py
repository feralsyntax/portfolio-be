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

admin.site.register(Technology)
admin.site.register(Feature)
admin.site.register(Industry)
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
