# Generated by Django 4.1.7 on 2023-02-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='message_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_data', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
    ]