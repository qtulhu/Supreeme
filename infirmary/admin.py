from django.contrib import admin
from .models  import Doctor,Pacient,Diagnosis,Procedure


admin.site.register(Doctor)
admin.site.register(Pacient)
admin.site.register(Diagnosis)
admin.site.register(Procedure)
