from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver


from unidecode import unidecode

class EmailSubs(models.Model):
    sub_email = models.CharField(('Abone Maili'), max_length=100)

    def __str__(self):
        return self.sub_email

    class Meta:
        verbose_name = "Bülten Abonesi"
        verbose_name_plural = "Bülten Aboneleri"

# Create your models here.
class MakaleTags(models.Model):
    makale_tag_isim = models.CharField(('Makale Tag'), max_length=100)

    def __str__(self):
        return self.makale_tag_isim

    class Meta:
        verbose_name = "Makale Etiketi"
        verbose_name_plural = "Makale Etiketleri"

class Makaleler(models.Model):
    makale_baslik = models.CharField(('Makale Başlığı'), max_length=150)
    makale_yayintarihi = models.DateField(('Makale Yayın Tarihi'))
    makale_mesaj = RichTextField()
    makale_slug = models.SlugField(unique=True)

    KATEGORILER = (
        ('hakaret', 'Hakaret'),
        ('yaralama', 'Yaralama'),
        ('orgutsuclari', 'Örgüt Suçları'),
        ('uyusturucumaddesuclari', 'Uyuşturucu Madde Suçları'),
        ('beyazyakalisuclari', 'Beyaz Yakalı Suçları'),
    )

    makale_kategori = models.CharField(('Makale Kategorisi'), max_length=50, choices=KATEGORILER)


    makale_meta_description = models.CharField(('Makale Meta Açıklaması(SEO İÇİN)'), max_length=350)

    tag = models.ManyToManyField(MakaleTags)

    ## MAKALE RESİMLERİ
    image625x400= models.ImageField(('625x400 Resim'))
    image297x400= models.ImageField(('297x400 Resim'))
    image240x160= models.ImageField(('240x160 Resim'))
    image500x287= models.ImageField(('500x287 ve 406x279 Resim'))
    image100x85= models.ImageField(('100x85 Resim'))

    def __str__(self):
        return self.makale_baslik

    def save(self, *args, **kwargs):

        self.makale_slug = slugify(unidecode(self.makale_baslik))
        super(Makaleler, self).save(*args, **kwargs)

    class Meta:
        ordering= ('-makale_yayintarihi',)
        verbose_name = "Makale"
        verbose_name_plural = "Makaleler"

@receiver(post_delete, sender=Makaleler)
def submission_delete(sender, instance, **kwargs):
    instance.image625x400.delete(False)
    instance.image297x400.delete(False)
    instance.image240x160.delete(False)
    instance.image500x287.delete(False)
    instance.image100x85.delete(False)
