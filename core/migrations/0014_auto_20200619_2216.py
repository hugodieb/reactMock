# Generated by Django 2.2.12 on 2020-06-19 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='template', to='core.Template'),
        ),
    ]
