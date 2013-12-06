from django.contrib import admin
from APIHandler.models import Product
from APIHandler.models import Caracteristic
from APIHandler.models import User
from APIHandler.models import Category

#Adding models to admin panel
admin.site.register(Product)
admin.site.register(Caracteristic)
admin.site.register(User)
admin.site.register(Category)

# Register your models here.
