# Generated by Django 4.1.3 on 2022-11-15 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0005_alter_queries_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queries',
            name='date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='queries',
            name='time',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]