from django.contrib import admin
from .models import Application

#check suites
# Optionally customize the admin interface
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'waitlist_position')  # Fields to display in the list view
    list_filter = ('status',)  # Filters you can use to sort data in the admin interface
    search_fields = ('user__username', 'status')  # Fields to search in the admin

# Register the model with the admin site
admin.site.register(Application, ApplicationAdmin)
