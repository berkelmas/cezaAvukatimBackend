from django.contrib import admin
from .models import Makaleler, MakaleTags, EmailSubs
from django.contrib.auth.models import User, Group


class MakalelerAdmin(admin.ModelAdmin):
    exclude = ('makale_slug',)
admin.site.register(Makaleler, MakalelerAdmin)

class MakaleTagsAdmin(admin.ModelAdmin):
    pass
admin.site.register(MakaleTags, MakaleTagsAdmin)

class EmailSubsAdmin(admin.ModelAdmin):
    pass
admin.site.register(EmailSubs, EmailSubsAdmin)
