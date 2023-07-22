# Generated by Django 4.2.3 on 2023-07-22 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0002_signature_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signature',
            name='message',
        ),
        migrations.AddField(
            model_name='signature',
            name='full_name',
            field=models.CharField(default='', max_length=50, verbose_name='Nombre completo'),
        ),
        migrations.AddField(
            model_name='signature',
            name='message_text',
            field=models.CharField(default='', max_length=280, verbose_name='Contenido del mensaje'),
        ),
    ]
