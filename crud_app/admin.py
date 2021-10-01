from django.contrib import admin
from.models import CustomerDetails
# Register your models here.

@admin.register(CustomerDetails)
class UserAdmin(admin.ModelAdmin):
  list_display= ['id', 'name', 'email', 'address', 'city', 'zipcode']
