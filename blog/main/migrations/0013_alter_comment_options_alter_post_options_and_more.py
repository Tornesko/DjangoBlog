# Generated by Django 4.1.2 on 2022-10-17 11:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_remove_comment_prev_comment_comment_time_create_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="comment",
            options={"ordering": ("-time",)},
        ),
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ("-time_create",)},
        ),
        migrations.RemoveField(
            model_name="comment",
            name="time_create",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="time_update",
        ),
        migrations.AddField(
            model_name="comment",
            name="published",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="comment",
            name="time",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="date published"
            ),
            preserve_default=False,
        ),
    ]
