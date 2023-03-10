# Generated by Django 3.2.7 on 2021-09-01 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(blank=True, null=True, upload_to='media/files/')),
                ('is_public', models.BooleanField(default=False)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='techer_files', to='teacher.teacher')),
            ],
        ),
    ]
