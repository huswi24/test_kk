from django.db import models

# Create your models here.

class Sale(models.Model):

    familyname_kanji = models.CharField('苗字漢字', max_length=50)
    lastname_kanji = models.CharField('名前漢字', max_length=50)
    familyname_kana = models.CharField('苗字カナ', max_length=50)
    lastname_kana = models.CharField('名前カナ', max_length=50)
    zipCode = models.CharField('郵便番号', max_length=255)
    state = models.CharField('都道府県', max_length=255)
    address = models.CharField('住所', max_length=255)
    buildingName = models.CharField('建物名', max_length=255)
    # phoneNumber = models.PhoneNumberField("電話番号" , max_length=255)
    phoneNumber = models.CharField("電話番号" , max_length=25)
    mailAdrress = models.CharField('メールアドレス', max_length=255)
    stripeCode = models.CharField("ストライプコード", max_length=50 , blank=True)
    salesPrice = models.IntegerField()
    taxPrice = models.IntegerField()
    shippingPrice = models.IntegerField()
    discountPrice = models.IntegerField()
    created = models.DateTimeField('販売日', auto_now_add=True)
    available = models.BooleanField('発送済み',default=False)

    class Meta:
        verbose_name_plural = "売上データ"
