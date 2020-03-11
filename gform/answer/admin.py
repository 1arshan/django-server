from django.contrib import admin
from .models import *
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(AnswerInfo)
admin.site.register(SingleAns)
admin.site.register(LinearScaleAns)
admin.site.register(FileAns)
admin.site.register(MultiAns, ArrayModelAdmin)
admin.site.register(CheckboxAns, ArrayModelAdmin)


