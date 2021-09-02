# Generated by Django 3.2.7 on 2021-09-02 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('isbn', models.CharField(max_length=16)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.author')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
    ]
