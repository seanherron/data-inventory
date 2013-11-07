from django.contrib import admin

from .models import Bureau_Code, Program_Code

class Program_CodeAdmin(admin.ModelAdmin):
    list_display = ('agency', 'program_name', 'program_code')

admin.site.register(Bureau_Code)
admin.site.register(Program_Code, Program_CodeAdmin)