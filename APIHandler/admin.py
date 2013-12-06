from django.contrib import admin
from APIHandler.models import Product
from APIHandler.models import Caracteristic
from APIHandler.models import User

#Adding models to admin panel
admin.site.register(Product)
admin.site.register(Caracteristic)
admin.site.register(User)

# Register your models here.
