from django.contrib import admin
from .models import Form, Contact
from .forms import ContactForm

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm

class FormAdmin(admin.ModelAdmin):
    ordering = ['first_name', 'last_name']
    readonly_fields = ('first_name', 'last_name', 'email', 'date', 'occupation')
    list_display = ('first_name', 'last_name', 'email', 'date', 'occupation')
    list_filter = ('date', 'occupation')

admin.site.register(Form, FormAdmin)
admin.site.register(Contact, ContactAdmin)
