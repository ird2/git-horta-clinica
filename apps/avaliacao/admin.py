from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pre_loader', {'fields': ('titulo_banner','descricao_banner','banner_imagem')}),

    )

    list_display = ('titulo_banner','descricao_banner','banner_imagem')


admin.site.register(Banner, BannerAdmin)

