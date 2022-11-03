from user.models import User
from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(_("Category name"), max_length=50)

    desc = models.CharField(_("Description"),
                            max_length=255,
                            null=True,
                            blank=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(_("Company name"), max_length=50)
    details = models.TextField(_("Details"))
    email = models.EmailField(_("Email ID"), max_length=254)
    phone_number = models.CharField(_("Phone number"), max_length=15)
    logo = models.FileField(_("Logo"), max_length=100)
    address_1 = models.CharField(_("Address Line 1"),
                                 max_length=50,
                                 null=True,
                                 blank=True)
    address_2 = models.CharField(_("Address Line 2"),
                                 max_length=50,
                                 null=True,
                                 blank=True)
    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=50)
    category = models.ForeignKey(Category,
                                 verbose_name=_("Category"),
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)

    managed_by = models.ForeignKey(User,
                                   verbose_name=_("Managed By"),
                                   on_delete=models.SET_NULL,null=True)

    rating = models.SmallIntegerField(_("Rating"), default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'


class Deal(models.Model):
    company = models.ForeignKey(Company,
                                verbose_name=_("Company"),
                                on_delete=models.CASCADE)

    title = models.CharField(_("Title"), max_length=50)
    desc = models.TextField(_("Description"))
    banner = models.ImageField(_("Banner"), max_length=None)

    points = models.BigIntegerField(_("Estimated points"), default=0)

    city = models.CharField(_("City"), max_length=50, null=True, blank=True)
    country = models.CharField(_("Country"), max_length=50)
    start_date = models.DateField(_("Start Date"),
                                  auto_now=False,
                                  auto_now_add=False)
    end_date = models.DateField(_("End Date"),
                                auto_now=False,
                                auto_now_add=False)
    offer = models.FloatField(_("Offer"))
    is_percentage = models.BooleanField(_("Is Percentage"), default=True)
    rating = models.SmallIntegerField(_("Rating"), default=0)

    class Meta:
        verbose_name = _("Deal")
        verbose_name_plural = _("Deals")

    def __str__(self):
        return self.title
