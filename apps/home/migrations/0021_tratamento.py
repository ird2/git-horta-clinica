# Generated by Django 3.0.8 on 2020-07-20 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200720_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tratamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem1', models.ImageField(blank=True, null=True, upload_to='home_tratamento')),
                ('seo_imagem1', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('imagem2', models.ImageField(blank=True, null=True, upload_to='home_sobre')),
                ('seo_imagem2', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('titulo1', models.CharField(default='', max_length=20)),
                ('titulo2', models.CharField(default='', max_length=30)),
                ('descricao', models.TextField(blank=True, default='', null=True)),
                ('ico1', models.ImageField(blank=True, null=True, upload_to='home_tratamento')),
                ('seo_ico1', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('titulo_ico1', models.CharField(default='', max_length=20)),
                ('descricao_ico1', models.TextField(blank=True, default='', null=True)),
                ('ico2', models.ImageField(blank=True, null=True, upload_to='home_tratamento')),
                ('seo_ico2', models.CharField(blank=True, default='', max_length=60, null=True)),
                ('titulo_ico2', models.CharField(default='', max_length=20)),
                ('descricao_ico2', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
