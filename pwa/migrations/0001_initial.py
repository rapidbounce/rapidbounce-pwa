# Generated by Django 3.2.16 on 2023-01-08 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PWASettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('title_el', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=255)),
                ('description_en', models.CharField(max_length=255, null=True)),
                ('description_el', models.CharField(max_length=255, null=True)),
                ('color', models.CharField(help_text='Color in hex. e.g #f08743', max_length=7)),
            ],
        ),
    ]