# Generated by Django 4.1 on 2022-11-18 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_book_date_of_issue_alter_book_count_alter_book_name'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(help_text='Books written/co-written by this author.<br>', related_name='authors', to='book.book'),
        ),
    ]