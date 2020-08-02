from django.contrib import admin
from .models import Banner,Oferta,Lista_Ofertas

class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pre_loader', {'fields': ('titulo_banner','descricao_banner','banner_imagem')}),

    )

    list_display = ('titulo_banner','descricao_banner','banner_imagem')


admin.site.register(Banner, BannerAdmin)

class OfertaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados Oferta', {'fields':
    ('titulo','imagem','seo_oferta','data_inicio','data_fim','descricao','desconto')}),

    )

    list_filter = ('titulo', 'data_inicio','data_fim')
    list_display = ('titulo','imagem','seo_oferta','data_inicio','data_fim','desconto','descricao')
    search_fields = ('titulo','data_inicio','data_fim' )


admin.site.register(Oferta, OfertaAdmin)
class Lista_OfertasAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pre_loader', {'fields': ('descricao','preco','pertence')}),

    )

    list_filter = ('descricao','pertence')
    list_display = ('descricao','preco','pertence')
    search_fields = ('descricao','pertence')


admin.site.register(Lista_Ofertas, Lista_OfertasAdmin)



