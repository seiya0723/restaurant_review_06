# Generated by Django 3.2.11 on 2022-02-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20220212_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='judge_dt',
            field=models.DateTimeField(blank=True, null=True, verbose_name='審査日時'),
        ),
    ]
