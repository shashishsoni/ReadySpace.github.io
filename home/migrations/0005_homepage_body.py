# Generated by Django 5.0.1 on 2024-01-14 15:40

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_homepage_banner_background_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "titel",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Text to deispaly", required=True
                                    ),
                                )
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
