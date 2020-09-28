# Generated by Django 3.1 on 2020-09-28 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dumps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=2, max_digits=100)),
                ('file', models.FileField(upload_to='portfolio/dumps')),
            ],
        ),
    ]
