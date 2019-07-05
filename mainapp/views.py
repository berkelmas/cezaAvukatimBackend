from rest_framework import generics
from rest_framework import filters

from .serializers import MakaleSerializer, EmailSubsSerializer, MakaleSerializerNoContent
from .models import Makaleler, MakaleTags, EmailSubs

from .paginations import YayinlarPagePagination, \
                                    MainPageLittleArticlesPagination

class MakaleDetail(generics.RetrieveAPIView): # detail page ( 1 item )
    queryset= Makaleler.objects.all()
    serializer_class= MakaleSerializer

class KategoriMakaleFilter(generics.ListAPIView):
    serializer_class= MakaleSerializer
    pagination_class = YayinlarPagePagination
    def get_queryset(self):
        queryset = Makaleler.objects.all()
        kategori = self.request.query_params.get('kategori', None)
        if kategori is not None:
            queryset = queryset.filter(makale_kategori=kategori)
        return queryset

class MainPageMakalelerNoContent(generics.ListAPIView):
    serializer_class= MakaleSerializerNoContent
    pagination_class= MainPageLittleArticlesPagination
    queryset= Makaleler.objects.all()

class AddEmailSub(generics.CreateAPIView):
    serializer_class= EmailSubsSerializer
