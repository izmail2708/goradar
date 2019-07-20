# Generated by Django 2.2.3 on 2019-07-17 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('report', '0005_auto_20190717_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_type', models.CharField(max_length=200)),
                ('report_tittle', models.CharField(max_length=200)),
                ('report_text', models.TextField()),
                ('report_published_date', models.DateTimeField()),
                ('reprot_likes', models.IntegerField(default=0)),
                ('report_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments_text', models.TextField()),
                ('comments_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.Report')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
