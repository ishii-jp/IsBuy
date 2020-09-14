from django.contrib import admin
from .models import Requests
from .models import RequestComment
from .models import RequestCategory
# Register your models here.
admin.site.register(Requests)
admin.site.register(RequestComment)
admin.site.register(RequestCategory)
