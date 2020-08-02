# Generated by Django 3.0.8 on 2020-07-24 12:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ofertas', '0002_oferta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista_Ofertas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(default='', max_length=30)),
                ('Preco', models.CharField(default='', max_length=30)),
                ('pertence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ofertas.Oferta')),
            ],
        ),
    ]