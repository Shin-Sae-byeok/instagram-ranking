# Generated by Django 3.0.8 on 2020-08-03 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='just_insta_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='insta_user_data',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta_user.just_insta_id'),
        ),
    ]
