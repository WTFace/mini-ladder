from django.contrib import admin
from .models import Result
from django.contrib.auth.models import User, Group


same_start = {'L':'홀','R':'짝'}
diff_start = {'L':'짝','R':'홀'}

class ResultAdmin(admin.ModelAdmin):
    list_display = ['id','start', 'bridges','end']
    list_filter = ['start']
    list_editable = ['start','bridges']

    
    def end(self, obj):
        return diff_start[obj.start] if obj.bridges==3 else same_start[obj.start]

    end.short_description = '결과'


admin.site.register(Result, ResultAdmin)
admin.site.unregister(Group)
admin.site.unregister(User)