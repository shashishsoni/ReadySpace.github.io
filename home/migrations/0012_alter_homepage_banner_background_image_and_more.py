# Generated by Django 5.0.1 on 2024-01-20 18:48

import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail.snippets.blocks
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0011_alter_homepage_body"),
        ("wagtailcore", "0089_log_entry_data_json_null_to_object"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="banner_background_image",
            field=models.ForeignKey(
                help_text="The banner background image",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    (
                        "title",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        help_text="Text to display", required=True
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        help_text="Bold title text for this card. Max length of 100 characters.",
                                                        max_length=100,
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.TextBlock(
                                                        help_text="Optional text for this card. Max length is 255 characters.",
                                                        max_length=255,
                                                        required=False,
                                                    ),
                                                ),
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        help_text="Image will be automagically cropped 570px by 370px"
                                                    ),
                                                ),
                                                (
                                                    "link",
                                                    wagtail.blocks.StructBlock(
                                                        [
                                                            (
                                                                "link_text",
                                                                wagtail.blocks.CharBlock(
                                                                    default="More Details",
                                                                    max_length=50,
                                                                ),
                                                            ),
                                                            (
                                                                "internal_page",
                                                                wagtail.blocks.PageChooserBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                            (
                                                                "external_link",
                                                                wagtail.blocks.URLBlock(
                                                                    required=False
                                                                ),
                                                            ),
                                                        ],
                                                        help_text="Enter a link or select a page",
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "image_and_text",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Image the automagically cropped to 786px by 552px"
                                    ),
                                ),
                                (
                                    "image_alignment",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("left", "Image to the left"),
                                            ("right", "Image to the right"),
                                        ],
                                        help_text="Image on the left with text on the right. Or image on the right with text on the left.",
                                    ),
                                ),
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Max length of 60 characters.",
                                        max_length=60,
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.CharBlock(
                                        max_length=140, required=False
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="More Details",
                                                    max_length=50,
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "cta",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Max length of 200 characters.",
                                        max_length=200,
                                    ),
                                ),
                                (
                                    "link",
                                    wagtail.blocks.StructBlock(
                                        [
                                            (
                                                "link_text",
                                                wagtail.blocks.CharBlock(
                                                    default="More Details",
                                                    max_length=50,
                                                ),
                                            ),
                                            (
                                                "internal_page",
                                                wagtail.blocks.PageChooserBlock(
                                                    required=False
                                                ),
                                            ),
                                            (
                                                "external_link",
                                                wagtail.blocks.URLBlock(required=False),
                                            ),
                                        ]
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "testimonial",
                        wagtail.snippets.blocks.SnippetChooserBlock(
                            target_model="testimonials.Testimonial",
                            template="streams/testimonial.html",
                        ),
                    ),
                    (
                        "pricing_table",
                        streams.blocks.PricingTableBlock(
                            table_options={
                                "autoColumnSize": False,
                                "colHeaders": False,
                                "contextMenu": [
                                    "row_above",
                                    "row_below",
                                    "---------",
                                    "col_left",
                                    "col_right",
                                    "---------",
                                    "remove_row",
                                    "remove_col",
                                    "---------",
                                    "undo",
                                    "redo",
                                ],
                                "editor": "text",
                                "minSpareRows": 0,
                                "renderer": "text",
                                "rowHeaders": True,
                                "startCols": 4,
                                "startRows": 4,
                                "stretchH": "all",
                            }
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
        migrations.AlterField(
            model_name="homepage",
            name="button",
            field=models.ForeignKey(
                blank=True,
                help_text="Select an optional page to link to",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailcore.page",
            ),
        ),
    ]
