# Generated by Django 2.1.7 on 2020-02-04 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0006_auto_20200204_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionreply',
            name='parent_reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='connect.QuestionReply'),
        ),
    ]
