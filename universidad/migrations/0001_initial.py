# Generated by Django 5.1.3 on 2024-11-15 05:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('datos_legales', models.JSONField()),
                ('historia', models.TextField()),
                ('logros', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemInformacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.JSONField()),
                ('tipo', models.CharField(max_length=50)),
                ('etiquetas', models.JSONField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('universidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='universidad.universidad')),
            ],
        ),
    ]
