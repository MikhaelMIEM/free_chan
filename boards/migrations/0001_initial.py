# Generated by Django 3.0.2 on 2020-01-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='board name')),
                ('description', models.CharField(max_length=200, verbose_name='board description')),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=200, verbose_name='thread theme')),
                ('message', models.TextField(verbose_name='thread message')),
                ('date', models.DateField(verbose_name='thread creation date')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='reply creation date')),
                ('message', models.TextField(verbose_name='reply message')),
                ('email', models.CharField(max_length=254, verbose_name='author email')),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boards.Thread')),
            ],
        ),
    ]
