# Generated by Django 4.1.6 on 2023-10-05 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitcourse', '0002_noticepart_delete_noicepart'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('note', models.FileField(upload_to='pdf')),
            ],
        ),
    ]
