from django.contrib import admin
from .models import Bug_Category, Bug_Status, Bug_Priority, TD_Priority, TD_Status, \
    LT_Status, LT_Category, T_Status, T_Rank
# Register your models here.


admin.site.register(Bug_Priority)
admin.site.register(Bug_Category)
admin.site.register(Bug_Status)
admin.site.register(TD_Status)
admin.site.register(TD_Priority)
admin.site.register(LT_Status)
admin.site.register(LT_Category)
admin.site.register(T_Status)
admin.site.register(T_Rank)
