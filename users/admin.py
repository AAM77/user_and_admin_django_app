from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser
    ordering = ('email', 'first_name', 'last_name', 'url', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    list_display = ('email', 'first_name', 'last_name', 'url', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'url')
    readonly_fields = ('date_joined', 'last_login', )

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(MyUser, MyUserAdmin)