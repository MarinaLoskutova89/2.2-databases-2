# Generated by Django 3.2.8 on 2022-01-06 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20220107_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='articles.category'),
        ),
    ]
