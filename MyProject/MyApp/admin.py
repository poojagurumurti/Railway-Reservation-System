from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from MyApp.models import Reservation


# Register your models here.

admin.site.register(Reservation)
