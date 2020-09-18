# Generated by Django 3.0.3 on 2020-09-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200918_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('home', models.BooleanField(default=False)),
                ('statis', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Mahsulotlar',
            },
        ),
    ]