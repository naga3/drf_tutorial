# Generated by Django 2.2.4 on 2019-09-02 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='名前', max_length=100)),
                ('birth_date', models.DateField(blank=True, help_text='誕生日', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='更新日時')),
            ],
        ),
    ]