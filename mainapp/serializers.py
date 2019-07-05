from rest_framework import serializers
from .models import EmailSubs

class MakaleSerializer(serializers.Serializer):
    id= serializers.CharField()
    makale_baslik = serializers.CharField(max_length=150)
    makale_yayintarihi = serializers.DateField()
    makale_mesaj = serializers.CharField()
    makale_kategori = serializers.CharField(source='get_makale_kategori_display')
    makale_kategori_nondisplay = serializers.CharField(source='makale_kategori')
    makale_slug = serializers.SlugField(allow_blank=False)

    makale_meta_description = serializers.CharField(max_length=350)
    tag = serializers.StringRelatedField(many=True)

    image625x400= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image297x400= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image240x160= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image500x287= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image100x85= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)

class MakaleSerializerNoContent(serializers.Serializer):
    id= serializers.CharField()
    makale_baslik = serializers.CharField(max_length=150)
    makale_yayintarihi = serializers.DateField()

    makale_kategori = serializers.CharField(source='get_makale_kategori_display')
    makale_kategori_nondisplay = serializers.CharField(source='makale_kategori')
    makale_slug = serializers.SlugField(allow_blank=False)


    image625x400= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image297x400= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image240x160= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image500x287= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)
    image100x85= serializers.ImageField(max_length=None, allow_empty_file=False, use_url=False)

class EmailSubsSerializer(serializers.Serializer):
    sub_email = serializers.CharField(max_length= 100)

    def create(self, validated_data):
        return EmailSubs.objects.create(**validated_data)
