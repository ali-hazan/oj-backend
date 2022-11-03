from time import time
from django.db import models
from django.utils.translation import gettext as _

DURATION_MODE_CHOICES = (
    ("M", "Months"),
    ("D", "Days"),
    ("W", "Weeks"),
    ("Y", "Years"),
)


class Plan(models.Model):
    name = models.CharField(_("Plan name"), max_length=50)
    desc = models.CharField(_("Description"), max_length=250)
    price = models.CharField(_("Price"), max_length=50)
    created_at = models.DateTimeField(_("Created at"),
                                      auto_now=False,
                                      auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"),
                                      auto_now=True,
                                      auto_now_add=False)
    points = models.IntegerField(_("Total Points"))
    duration = models.PositiveIntegerField(_("Duration"))
    duration_mode = models.CharField(_("Duration mode"),
                                     max_length=1,
                                     choices=DURATION_MODE_CHOICES)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

class Benefit(models.Model):
    details = models.CharField(_("Benefit Details"), max_length=255)
    plan = models.ForeignKey(Plan, verbose_name=_("Plan"), on_delete=models.CASCADE)



    class Meta:
        verbose_name =  'Benefit'
        verbose_name_plural =  'Benefits'
