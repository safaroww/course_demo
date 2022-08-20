from django.contrib import admin
from .models import Tag, Course, Lesson

# Register your models here.


admin.site.register(Tag)
admin.site.register(Course)
admin.site.register(Lesson)