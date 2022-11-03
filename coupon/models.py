from django.db import models
from deals.models import Deal
from user.models import User
from django.utils.translation import gettext as _

class Coupon(models.Model):
    code = models.CharField(_("Coupon code"), max_length=10)
    deal = models.ForeignKey(Deal,
                             verbose_name=_("Deal"),
                             on_delete=models.SET_NULL,
                             null=True)

    requested_by = models.ForeignKey(User,
                                     verbose_name=_("Requested by"),
                                     on_delete=models.SET_NULL,
                                     null=True)
    is_approved = models.BooleanField(_("Is Approved"), default=True)

    is_climed = models.BooleanField(_("Coupon Climed"), default=False)

    expire_at = models.DateField(_("Expires at"))
    created_at = models.DateTimeField(_("Created at"),
                                      auto_now=False,
                                      auto_now_add=True)

    updated_at = models.DateTimeField(_("Updated at"),
                                      auto_now=True,
                                      auto_now_add=False)

    class Meta:
        verbose_name = _("Coupon")
        verbose_name_plural = _("Coupons")

    def __str__(self):
        return self.code
