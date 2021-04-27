from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from django.contrib.sessions.models import Session
import pprint

class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'

admin.site.register(Session, SessionAdmin)
>>>>>>> 1cd8cb2885fa20310957184f0f67ba12858b7678
