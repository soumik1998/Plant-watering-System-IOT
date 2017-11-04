from django.contrib import admin
from .models import Plants, User, Temp, Water, Soil, Actuator, Rain

admin.site.register(User)
admin.site.register(Plants)
admin.site.register(Temp)
admin.site.register(Water)
admin.site.register(Soil)
admin.site.register(Rain)
admin.site.register(Actuator)
