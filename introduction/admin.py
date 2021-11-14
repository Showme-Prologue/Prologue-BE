from django.contrib import admin

from .models import Introduction, IntroductionComponent, IntroductionQuestion

# Register your models here.

admin.site.register(Introduction)
admin.site.register(IntroductionComponent)
admin.site.register(IntroductionQuestion)