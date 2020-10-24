# Generated by Django 3.0.7 on 2020-10-24 08:07

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Company_buying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('contract', models.IntegerField()),
                ('title', models.CharField(max_length=200)),
                ('main_img', models.ImageField(upload_to='images/')),
                ('detail_img1', models.ImageField(null=True, upload_to='images/')),
                ('detail_img2', models.ImageField(null=True, upload_to='images/')),
                ('contents', models.TextField()),
                ('category', models.IntegerField()),
                ('apartment', models.CharField(max_length=100)),
                ('finish_date', models.DateField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Flee_market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('img1', models.ImageField(null=True, upload_to='images/')),
                ('img2', models.ImageField(null=True, upload_to='images/')),
                ('contents', models.TextField(null=True)),
                ('proceeding', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
                ('writer', models.IntegerField()),
                ('category', models.IntegerField()),
                ('apartment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group_buying',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('img', models.ImageField(null=True, upload_to='images/')),
                ('proceeding', models.IntegerField()),
                ('contents', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('writer', models.IntegerField()),
                ('category', models.IntegerField()),
                ('apartment', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Group_buying_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_buying_id', models.IntegerField()),
                ('user_info_id', models.IntegerField()),
                ('contents', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_id', models.IntegerField()),
                ('writer', models.IntegerField()),
                ('grade', models.FloatField()),
                ('contents', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('nickname', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]