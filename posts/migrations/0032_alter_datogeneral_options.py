# Generated by Django 4.0.4 on 2022-09-14 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0031_rename_protresta_ciudadana_datogeneral_protesta_ciudadana'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datogeneral',
            options={'ordering': ['homoclave']},
        ),
    ]
