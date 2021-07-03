from django.contrib import admin
from . models import message
from . models import usign
from . models import asign
from . models import uaddevent
from . models import proedituser 
from . models import adevents
from . models import Manualbooking
from . models import adminuser

# Register your models here.
admin.site.register(message)
admin.site.register(usign)
admin.site.register(asign)
admin.site.register(uaddevent)
admin.site.register(proedituser)
admin.site.register(adevents)
admin.site.register(Manualbooking)
admin.site.register(adminuser)
