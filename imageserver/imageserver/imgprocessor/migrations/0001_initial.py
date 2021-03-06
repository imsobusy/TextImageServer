# Generated by Django 3.0.8 on 2020-07-30 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientImageRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, default='Empty Title', max_length=128)),
                ('content', models.TextField(blank=True, default='Empty Content', max_length=512)),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='TextImageResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(blank=True, default='Empty Title', max_length=128)),
                ('content', models.TextField(blank=True, default='Empty Content', max_length=512)),
                ('imageUrl', models.ImageField(upload_to='uploads/')),
            ],
            options={
                'ordering': ['createdAt'],
            },
        ),
        migrations.CreateModel(
            name='NameFields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('clientImageRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imgprocessor.ClientImageRequest')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
