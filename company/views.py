from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    if len(value) != 12 or value[:2] != '+7' or not value[1:].isdigit():
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value}
        )

