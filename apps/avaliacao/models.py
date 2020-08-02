from django.db import models


class Banner(models.Model):
    titulo_banner = models.CharField(max_length=30, default='')
    descricao_banner = models.TextField(null=True, blank=True, default='')

    banner_imagem = models.ImageField(upload_to='avalicao_imagem', null=True, blank=True)

    def __str__(self):
        return self.titulo_banner
