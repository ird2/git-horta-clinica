from django.db import models


class Banner(models.Model):
    titulo_banner = models.CharField(max_length=30, default='')
    descricao_banner = models.TextField(null=True, blank=True, default='')

    banner_imagem = models.ImageField(upload_to='tratamentos_imagens', null=True, blank=True)

    def __str__(self):
        return self.titulo_banner

class Tratamento(models.Model):
    titulo = models.CharField(max_length=30, default='')
    imagem = models.ImageField(upload_to='oferta_images', null=True, blank=True)
    seo_tratamento = models.CharField(max_length=100, default='')
    descricao = models.TextField(null=True, blank=True, default='')


    def __str__(self):
        return self.titulo