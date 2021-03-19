from django.contrib import admin
from purchase.models import Sale


class SalesAdmin(admin.ModelAdmin):
    list_display = ('created', 'salesPrice', 'state', 'familyname_kanji',)  # 一覧に出したい項目
    readonly_fields = ('created','salesPrice','taxPrice','shippingPrice','discountPrice','stripeCode')
   

admin.site.register(Sale,SalesAdmin)
