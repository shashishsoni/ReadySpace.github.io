from django.db import models

from wagtail.contrib.forms.models  import AbstractEmailForm, AbstractFormField
from django.utils.translation import gettext_lazy as _
from wagtail.admin.panels import FieldPanel, InlinePanel

from modelcluster.models import ParentalKey

from wagtail.fields import RichTextField

# Create your models here.

FORM_FIELD_CHOICES = (
    ("singleline", _("Single line text")),
    ("multiline", _("Multi-line text")),
    ("email", _("Email")),
    ("number", _("Number")),
    ("url", _("URL")),
    ("checkboxes", _("Checkboxes")),
    ("dropdown", _("Drop down")),
    ("multiselect", _("Multiple select")),
    ("date", _("Date")),
    ("datetime", _("Date/time")),
)


class CustomAbstractFormField(AbstractFormField):
    field_type = models.CharField(
        verbose_name = "Field Type",
        max_length = 16,
        choices = FORM_FIELD_CHOICES,
    )
    
    class Meta:
        abstract = True,
        ordering = ["sort_order"]


class FromField(CustomAbstractFormField):
    page = ParentalKey(
        "ContactPage",
        on_delete = models.CASCADE,
        related_name = "form_fields" 
    )


class ContactPage(AbstractEmailForm):
    
    template = "contact/contact_page.html"
    landing_page_template = "contact/contact_page_landing.html"
    subpage_types = []
    max_count = 1
    
    intro = RichTextField(
        blank = True, 
        features = ["bold", "link", "ol", "ul"]
    )
    thank_you_text = RichTextField(
        blank = True,
        features = ["bold", "link", "ol", "ul"]
    )
    map_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank = False,
        on_delete = models.SET_NULL,
        help_text = "image will be cropped to 580px by 355px",
        related_name = '+',
    )
    map_url = models.URLField(
        blank = True,
        help_text = "Optional. If you provided a link here the map image will become a link"
    )
    

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel("intro"),
        FieldPanel("map_image"),
        FieldPanel("map_url"),
        InlinePanel("form_fields", label='Form Fields'),
        FieldPanel("thank_you_text"),
        FieldPanel("from_address"),
        FieldPanel("to_address"),
        FieldPanel("subject"),
    ]