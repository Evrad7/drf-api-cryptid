# Generated by Django 5.0.6 on 2024-07-10 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_comment', '0001_initial'),
        ('core_post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core_post.post'),
        ),
    ]
