from django.contrib import admin

from .models import Signature



class SignatureAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'message_text', 'pub_date', 'status')

admin.site.register(Signature, SignatureAdmin)