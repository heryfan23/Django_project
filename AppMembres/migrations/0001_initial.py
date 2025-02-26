# Generated by Django 5.0.6 on 2024-07-15 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('pseudo', models.CharField(max_length=50)),
                ('prenom', models.TextField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.TextField()),
                ('photo', models.ImageField(upload_to='static/images/membres/')),
                ('date_inscrit', models.DateTimeField()),
            ],
        ),
    ]
