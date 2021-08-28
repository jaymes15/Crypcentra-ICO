from django.contrib import admin
from django.apps import apps


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.site_header = 'Crypcentra ICO Admin'
