# Generated by Django 3.0.8 on 2020-07-19 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200719_1413'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rodape',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_rodape', models.ImageField(blank=True, null=True, upload_to='menu_logo')),
                ('seo_logo_rodape', models.CharField(blank=True, default='', max_length=45, null=True)),
                ('descricao_rodape', models.TextField(blank=True, default='', null=True)),
                ('horario', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='preloader_site',
            name='descricao_preloader',
        ),
    ]