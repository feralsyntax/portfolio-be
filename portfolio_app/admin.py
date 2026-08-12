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

admin.site.register(Project)
admin.site.register(Technology)
admin.site.register(Feature)
admin.site.register(Industry)
admin.site.register(Detail)
admin.site.register(KeyFeature)
admin.site.register(Challenge)
admin.site.register(Impact)
