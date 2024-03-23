# Generated by Django 4.0.2 on 2024-03-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='profile_photos/')),
                ('membership_start_date', models.DateField()),
                ('membership_end_date', models.DateField()),
            ],
        ),
    ]
