# Generated by Django 4.0.4 on 2022-07-27 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0019_blogs_draft_alter_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='draft',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=5, null=True),
        ),
    ]
