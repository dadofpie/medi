from django.contrib import admin

# Register your models here.


from .models import vatProvision, memTypes, prinMem, relaMem, Member
from .models import modeOfPayment,parentCompany,accountStatus,company
from .models import  productType,account



from .models import planList

from django import forms

from django.contrib import admin

# Remove Group Model from admin. We're not using it.
admin.site.register(planList)
admin.site.register(productType)
admin.site.register(company)
admin.site.register(accountStatus)
admin.site.register(parentCompany)

admin.site.register(modeOfPayment)
admin.site.register(vatProvision)
admin.site.register(account)
admin.site.register(memTypes)
admin.site.register(prinMem)
admin.site.register(relaMem)
admin.site.register(Member)


