from django.contrib import admin
from .models import Intro, Resume, MySkill, MyProject

# Register your models here.
admin.site.register(Intro)
admin.site.register(Resume)
admin.site.register(MySkill)
admin.site.register(MyProject)