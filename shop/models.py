from django.db import models

# Create your models here.
from django.urls import reverse

class ShippingPrice(models.Model):
    area_name = models.CharField("エリア名",max_length=20,unique=True)
    shipping_price = models.IntegerField("配送料")
    description = models.TextField("エリア説明",blank=True)
    

    class Meta:
        ordering = ('area_name',)
        verbose_name_plural = "配送料"
    
    def __str__(self):
        return self.area_name

    


class Category(models.Model):
    name = models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="category",blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "カテゴリー"

    def get_url(self):
        return reverse('shop:products_by_category', args=[self.slug])

    def __str__(self):
        return "{}".format(self.name)


class Product(models.Model):
    name = models.CharField("商品名",max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    description = models.TextField("商品説明",blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.PositiveIntegerField("価格")
    inTax = models.PositiveIntegerField("内消費税",default=200)
    image = models.ImageField("TOP画像",upload_to="product",blank=True)
    stock = models.IntegerField("在庫")
    available = models.BooleanField(default=True)
    created = models.DateTimeField("作成日",auto_now_add=True)
    updated = models.DateTimeField("変更日",auto_now=True)

    cartDescription = models.TextField("カート用説明", max_length=100,blank=True)#New)
    image2 = models.ImageField("画像2枚目",upload_to="product",blank=True)#New
    image3 = models.ImageField("画像3枚目",upload_to="product",blank=True)#New
    hoverImage = models.ImageField("ホバー画像",upload_to="product",blank=True)#New
    cookingUrl = models.CharField("調理動画",max_length=10000,blank=True)#New

    descriptionTitle1 = models.CharField("説明タイトル1",max_length=255, blank=True)#New
    descriptionContent1 = models.TextField("説明内容1",blank=True)#New
    descriptionImage1 = models.ImageField("説明画像1",upload_to="product", blank=True)#New

    descriptionTitle2 = models.CharField("説明タイトル2",max_length=255, blank=True)#New
    descriptionContent2 = models.TextField("説明タイトル2",blank=True)#New
    descriptionImage2 = models.ImageField("説明画像2",upload_to="product",blank=True)#New

    descriptionTitle3 = models.CharField("説明タイトル3",max_length=255,blank=True)#New
    descriptionContent3 = models.TextField("説明内容3",blank=True)#New
    descriptionImage3 = models.ImageField("説明画像3",upload_to="product",blank=True)#New

    descriptionTitle4 = models.CharField("説明タイトル4",max_length=255,blank=True)#New
    descriptionContent4 = models.TextField("説明内容4",blank=True)#New
    descriptionImage4 = models.ImageField("説明画像4",upload_to="product",blank=True)#New
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "商品データ"


    def get_url(self):
        return reverse('shop:ProdCatDetail', args=[self.category.slug, self.slug])


    def __str__(self):
        return str(self.name)