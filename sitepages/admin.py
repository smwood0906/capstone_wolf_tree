from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from beerfinder.models import Vendor, Type, Beer
from blog.models import Category, Post
# Register your models here.



class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """

    def confirm_login_allowed(self, user):

    # remove ‘or not user.is_staff’ from check
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages["invalid_login"],
            code ="invalid_login",
            params = {"username": self.username_field.verbose_name}
            )

class UserAdmin(AdminSite):
    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active

from schedule.models import Calendar, Event, CalendarRelation, Rule
from schedule.forms import EventAdminForm

class CalendarAdminOptions(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']


class EventAdmin(admin.ModelAdmin):
    form = EventAdminForm

user_admin_site = UserAdmin(name='usersadmin')
user_admin_site.register(Calendar, CalendarAdminOptions)
user_admin_site.register(Event, EventAdmin)
user_admin_site.register([Rule, CalendarRelation])


user_admin_site.register(Vendor)
user_admin_site.register(Type)
user_admin_site.register(Beer)
user_admin_site.register(Category)
user_admin_site.register(Post)
