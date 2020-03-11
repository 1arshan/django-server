from django.contrib import admin
from .models import *
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin


class ArrayModelAdmin(admin.ModelAdmin, DynamicArrayMixin):
    pass


admin.site.register(FormInfo)
admin.site.register(SingleAnsQues)
admin.site.register(FileQues)
admin.site.register(LinearScaleQues)
admin.site.register(MultiAnsQues, ArrayModelAdmin)
admin.site.register(CheckboxQues, ArrayModelAdmin)


