from django.contrib import admin
from .models import Empresa,Preloader_site,Rodape,Banner,Sobre,Tratamento,Videos


class Preloader_siteAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pre_loader', {'fields': ('titulo_preloader','logo_preloader','seo_logo_preloader')}),

    )

    list_filter = ('titulo_preloader','seo_logo_preloader')
    list_display = ('titulo_preloader','logo_preloader','seo_logo_preloader')
    search_fields = ('titulo_preloader','seo_logo_preloader')

admin.site.register(Preloader_site, Preloader_siteAdmin)

class EmpresaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados empresa', {'fields': ('nome_empresa','descricao_empresa','email', 'endereco','telefone','whatsapp','facebook','instagram','linkedln','logo', 'seo_logo')}),

    )


    list_display = ('nome_empresa','telefone','endereco','whatsapp','facebook','instagram','email', 'logo','seo_logo')



admin.site.register(Empresa, EmpresaAdmin)


class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pre_loader', {'fields': ('nome_banner','titulo1','titulo2','descricao','imagem','seo_banner')}),

    )


    list_filter = ('nome_banner','descricao')
    list_display = ('nome_banner','titulo1','titulo2','descricao','imagem','seo_banner')
    search_fields = ('nome_banner','descricao')

admin.site.register(Banner, BannerAdmin)

class sobreAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados sobre', {'fields': ('titulo1','titulo2','descricao','imagem1','seo_imagem1','imagem2','seo_imagem2','imagem3','seo_imagem3','imagem4','seo_imagem4')}),

    )

    list_display = ('titulo1','titulo2','descricao','imagem1','seo_imagem1','imagem2','seo_imagem2','imagem3','seo_imagem3','imagem4','seo_imagem4')


admin.site.register(Sobre, sobreAdmin)

class tratamentoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados sobre', {'fields': ('imagem_antes','seo_imagem_antes','imagem_depois','seo_imagem_depois','titulo1',
           'titulo2','descricao','ico1','seo_ico1','titulo_ico1','descricao_ico1',
            'ico2','seo_ico2','titulo_ico2','descricao_ico2')}),

    )


    list_display =('titulo1','titulo2','imagem_antes','seo_imagem_antes','imagem_depois','seo_imagem_depois','descricao','ico1','seo_ico1','titulo_ico1','descricao_ico1',
            'ico2','seo_ico2','titulo_ico2','descricao_ico2')
admin.site.register(Tratamento, tratamentoAdmin)

class videosAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados sobre', {'fields': ('nome','img_capa','url_video')}),

    )

    list_display =('nome','img_capa','url_video')
admin.site.register(Videos, videosAdmin)







class rodapeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados empresa', {'fields': ('descricao_rodape','logo_rodape','seo_logo_rodape','horario','horario2','horario3')}),

    )


    list_display = ('descricao_rodape','logo_rodape','seo_logo_rodape', 'horario','horario2','horario3')



admin.site.register(Rodape, rodapeAdmin)

