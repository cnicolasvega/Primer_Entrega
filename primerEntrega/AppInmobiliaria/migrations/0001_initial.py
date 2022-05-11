# Generated by Django 4.0.4 on 2022-05-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('pisos', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banos', models.IntegerField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Departamentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=200)),
                ('numero', models.IntegerField()),
                ('pisos', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('banos', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('expensas', models.IntegerField()),
            ],
        ),
    ]