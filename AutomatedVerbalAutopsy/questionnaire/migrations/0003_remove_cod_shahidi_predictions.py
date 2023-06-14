# Generated by Django 4.1.7 on 2023-06-08 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0002_cod_remove_uchunguzi_mhanga_remove_uchunguzi_shahidi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cod',
            name='shahidi',
        ),
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sababu', models.CharField(max_length=50)),
                ('cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='predictions', to='questionnaire.cod')),
            ],
        ),
    ]
