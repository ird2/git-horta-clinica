# Generated by Django 3.0.8 on 2020-07-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200719_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='descricao_empresa',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
