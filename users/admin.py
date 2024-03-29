from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.
#admin.site.register(Profile) se puede usar esta funcion para test

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number','website', 'picture')
    search_fields = ('user__email', 'user_username', 'user__first_name', 'user__last_name','phone_number')

    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )

    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),),
        }),
        ('Extra_info',{
            'fields':(
                ('website','phone_number'),
                ('biography'),
            ),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        }),
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile to base user admin"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)