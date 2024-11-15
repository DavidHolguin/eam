# Generated by Django 5.1.3 on 2024-11-15 05:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('tipo_documento', models.CharField(choices=[('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('PS', 'Pasaporte')], max_length=2)),
                ('numero_documento', models.CharField(max_length=20, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$')])),
                ('email_institucional', models.EmailField(max_length=254, unique=True)),
                ('email_personal', models.EmailField(blank=True, max_length=254)),
                ('rol', models.CharField(choices=[('DECANO', 'Decano'), ('DIRECTOR', 'Director de Programa'), ('DOCENTE', 'Docente'), ('ADMINISTRATIVO', 'Personal Administrativo')], max_length=20)),
                ('fecha_vinculacion', models.DateField()),
                ('activo', models.BooleanField(default=True)),
                ('titulo_academico', models.CharField(max_length=200)),
                ('especialidad', models.CharField(max_length=200)),
                ('cv_resumen', models.TextField()),
                ('foto', models.ImageField(blank=True, null=True, upload_to='team/fotos/')),
                ('metadata', models.JSONField(blank=True, default=dict)),
            ],
            options={
                'ordering': ['apellidos', 'nombres'],
                'indexes': [models.Index(fields=['numero_documento'], name='team_person_numero__27bf50_idx'), models.Index(fields=['email_institucional'], name='team_person_email_i_329c76_idx'), models.Index(fields=['rol'], name='team_person_rol_ec74cd_idx')],
            },
        ),
    ]
