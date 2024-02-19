from django.contrib import admin
from.models import user
from auditlog.registry import auditlog
from django.contrib.auth.models import User
# Register your models here.

admin.site.register(user)

auditlog.register(user,exclude_fields=['phone'],include_fields=['user'])

auditlog.register(User,include_fields=['username'])

# AUDITLOG_EXCLUDE_TRACKING_FIELDS = (
#     "created",
#     "modified"
# )


# from django.views.generic import DetailView
# from auditlog.mixins import LogAccessMixin 
# class MyModelDetailView(LogAccessMixin,DetailView):
#     model=user
    