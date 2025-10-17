from django.contrib import admin
from .models import Partita

admin.site.register(Partita)
print(Partita.objects.all())