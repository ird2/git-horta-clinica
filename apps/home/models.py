from django.db import models


class Preloader_site(models.Model):
    titulo_preloader = models.CharField(max_length=30, default='')
    logo_preloader = models.ImageField(upload_to='menu_logo', null=True, blank=True)
    seo_logo_preloader = models.CharField(max_length=45, null=True, blank=True, default='')

    def __str__(self):
        return self.titulo_preloader

class Empresa(models.Model):
    nome_empresa=models.CharField(max_length=30 , default='', help_text='Nome da empresa' )
    descricao_empresa = models.TextField(null=True, blank=True, default='')
    email = models.CharField(max_length=30,null=True, blank=True)
    endereco = models.CharField(max_length=70,null=True, blank=True)
    telefone = models.CharField(max_length=30,null=True, blank=True)
    whatsapp = models.CharField(max_length=30,null=True, blank=True, default='')
    facebook =models.CharField(max_length=60 ,null=True, blank=True, default='' )
    instagram = models.CharField(max_length=60,null=True, blank=True, default='')
    linkedln = models.CharField(max_length=60, null=True, blank=True,default='')


    logo = models.ImageField(upload_to='menu_logo', null=True, blank=True)
    seo_logo = models.CharField(max_length=45,null=True, blank=True,default='')


    def __str__(self):
        return self.email

class Banner(models.Model):
    nome_banner=models.CharField(max_length=30 , default='' )
    titulo1=models.CharField(max_length=20 , default='' )
    titulo2 = models.CharField(max_length=30, default='')

    descricao= models.TextField(null=True, blank=True, default='')

    imagem = models.ImageField(upload_to='menu_banner', null=True, blank=True)
    seo_banner = models.CharField(max_length=45,null=True, blank=True,default='')


    def __str__(self):
        return self.nome_banner


class Sobre(models.Model):

    titulo1=models.CharField(max_length=20 , default='' )
    titulo2 = models.CharField(max_length=30, default='')

    descricao= models.TextField(null=True, blank=True, default='')

    imagem1 = models.ImageField(upload_to='home_sobre', null=True, blank=True)
    seo_imagem1 = models.CharField(max_length=60,null=True, blank=True,default='')

    imagem2 = models.ImageField(upload_to='home_sobre', null=True, blank=True)
    seo_imagem2 = models.CharField(max_length=60, null=True, blank=True, default='')

    imagem3 = models.ImageField(upload_to='home_sobre', null=True, blank=True)
    seo_imagem3 = models.CharField(max_length=60, null=True, blank=True, default='')

    imagem4 = models.ImageField(upload_to='home_sobre', null=True, blank=True)
    seo_imagem4 = models.CharField(max_length=60, null=True, blank=True, default='')

    def __str__(self):
        return self.titulo1

class Tratamento(models.Model):
    imagem_antes = models.ImageField(upload_to='home_tratamento', null=True, blank=True)
    seo_imagem_antes = models.CharField(max_length=60, null=True, blank=True, default='')

    imagem_depois = models.ImageField(upload_to='home_tratamento', null=True, blank=True)
    seo_imagem_depois = models.CharField(max_length=60, null=True, blank=True, default='')

    titulo1=models.CharField(max_length=20 , default='' )
    titulo2 = models.CharField(max_length=30, default='')
    descricao= models.TextField(null=True, blank=True, default='')

    ico1= models.ImageField(upload_to='home_tratamento', null=True, blank=True)
    seo_ico1 = models.CharField(max_length=60, null=True, blank=True, default='')
    titulo_ico1 = models.CharField(max_length=20, default='')
    descricao_ico1= models.TextField(null=True, blank=True, default='')

    ico2 = models.ImageField(upload_to='home_tratamento', null=True, blank=True)
    seo_ico2 = models.CharField(max_length=60, null=True, blank=True, default='')
    titulo_ico2 = models.CharField(max_length=20, default='')
    descricao_ico2 = models.TextField(null=True, blank=True, default='')

    def __str__(self):
        return self.titulo1

class Videos(models.Model):
        nome = models.CharField(max_length=150, default='')
        img_capa = models.ImageField(upload_to='home_video', null=True, blank=True)
        url_video = models.CharField(max_length=150, default='')
        def __str__(self):
            return self.nome





class Rodape(models.Model):
    logo_rodape = models.ImageField(upload_to='menu_logo', null=True, blank=True)
    seo_logo_rodape = models.CharField(max_length=45, null=True, blank=True, default='')
    descricao_rodape = models.TextField(null=True, blank=True, default='')
    horario= models.CharField(max_length=45, null=True, blank=True, default='')
    horario2 = models.CharField(max_length=45, null=True, blank=True, default='')
    horario3 = models.CharField(max_length=45, null=True, blank=True, default='')


    def __str__(self):
        return self.descricao_rodape
