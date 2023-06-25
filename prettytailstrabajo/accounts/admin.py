from django.contrib import admin
<<<<<<< HEAD
from django.contrib.auth.models import User
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user','first_name','last_name','rut_user', 'address', 'location', 'telephone', 'user_group')
=======
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'address', 'location', 'telephone', 'user_group')
>>>>>>> f37be34e12396f6c2c65534768d11806d03a7709
    search_fields =('location', 'user__username', 'user__groups__name')
    list_filter = ('user__groups', 'location')

    def user_group(self, obj):
        return " - ".join([t.name for t in obj.user.groups.all().order_by('name')])

    user_group.short_description = 'Grupo'

admin.site.register(Profile, ProfileAdmin)