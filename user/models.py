from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.db import models
from plan.models import Plan


class User(AbstractUser):
    phone_number = models.CharField(_("Phone number"),
                                    max_length=15,
                                    null=True,
                                    blank=True)
    available_loyality_point = models.BigIntegerField(
        _("Available Loyality point"), default=0)

    subscribed = models.ForeignKey(Plan,
                                   verbose_name=_("Plan"),
                                   on_delete=models.SET_NULL,
                                   blank=True,
                                   null=True)

    subscribedAt = models.DateField(verbose_name=_("Subscribed At"),
                                    null=True,
                                    blank=True)

    subscribedExpire = models.DateField(verbose_name=_("Subscribed Expire"),
                                        null=True,
                                        blank=True)

    is_company_admin = models.BooleanField(_("Is company Admin"),
                                           default=False)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
