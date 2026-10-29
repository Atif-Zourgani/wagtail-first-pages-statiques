
from django.db import models
# fieldpannel affiche un champs dans l'admin 
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page

class HomePage(Page):
    # une ligne de text de 255 charac 
    accroche = models.CharField(max_length=255, blank=True)
    # paragraphe avec mise en forme 
    introduction = RichTextField(blank=True)
    # boolean (true ou false) 
    disponible = models.BooleanField(default=False)
    # decimal avec specificité 
    prix = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    # une date de début 
    date_debut = models.DateField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("accroche"),
        FieldPanel("introduction"),
        FieldPanel("disponible"),
        FieldPanel("prix"),
        FieldPanel("date_debut")
    ]