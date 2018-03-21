from django.contrib import admin
from .models import User, Player, Setting, League, Transaction, Asset

admin.site.register(User)
admin.site.register(Player)
admin.site.register(Setting)
admin.site.register(League)
admin.site.register(Transaction)
admin.site.register(Asset)
# Register your models here.
