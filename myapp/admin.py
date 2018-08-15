#superuser account: USERNAME=admin, EMAIL=admin@nlv.com, PSW=adminpassword

from django.contrib import admin
from .models import Videogame

admin.site.register(Videogame)
