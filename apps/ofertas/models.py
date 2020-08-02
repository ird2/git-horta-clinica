from django.db import models


class Banner(models.Model):
    titulo_banner = models.CharField(max_length=30, default='')
    descricao_banner = models.TextField(null=True, blank=True, default='')

    banner_imagem = models.ImageField(upload_to='avalicao_imagem', null=True, blank=True)

    def __str__(self):
        return self.titulo_banner


class Oferta(models.Model):
    titulo = models.CharField(max_length=30, default='')
    descricao = models.TextField(null=True, blank=True, default='')
    desconto = models.DecimalField(decimal_places=2, max_digits=7)
    imagem = models.ImageField(upload_to='oferta_images', null=True, blank=True)
    seo_oferta = models.CharField(max_length=30, default='')

    data_inicio=models.DateField(null=True, blank=True)
    data_fim=models.DateField(null=True, blank=True)


    def __str__(self):
        return self.titulo

class Lista_Ofertas(models.Model):
    descricao = models.CharField(max_length=30, default='')
    preco = models.DecimalField(decimal_places=2, max_digits=7)
    pertence = models.ForeignKey(Oferta, on_delete=models.CASCADE)


    def __str__(self):
        return self.descricao




