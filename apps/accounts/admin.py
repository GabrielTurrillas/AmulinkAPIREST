from django.contrib import admin
from .models import UserAccount

# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_per_page = 25

admin.site.register(UserAccount, UserAccountAdmin)
