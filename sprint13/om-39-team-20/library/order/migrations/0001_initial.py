# Generated by Django 4.1 on 2022-11-12 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('plated_end_at', models.DateTimeField()),
                ('end_at', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser')),
            ],
        ),
    ]
