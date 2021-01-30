from django.contrib import admin
from .models import User, organization, bug

# Register your models here.
class UserAdmin(admin.ModelAdmin): 
    model = User
admin.site.register(User, UserAdmin)
admin.site.register(organization) # 
admin.site.register(bug)