from typing import Any
from django import forms
from django.forms import DecimalField, TextInput
from diary.models import Diary
from django.core.exceptions import ValidationError
import datetime


class AddActivityForm(forms.ModelForm):
    TRANSACTION_TYPE = (
        ("G", "Gasto"),
        ("I", "Ingreso"),
    )
    activity_date = forms.DateField(initial=datetime.date.today)
    activity = forms.CharField(widget=forms.Textarea(attrs={"rows": 3, "cols": 40}))
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPE)
    debit = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=TextInput(attrs={"type": "number"}),
        required=False,
    )

    credit = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=TextInput(attrs={"type": "number}"}),
        required=False,
    )

    class Meta:
        model = Diary
        fields = [
            "activity_date",
            "activity",
            "transaction_type",
            "debit",
            "credit",
            "reference",
            "balance",
        ]
        exclude = (
            "is_active",
            "farm",
        )

    def clean(self):
        cleaned_data = super().clean()
        transaction_type = cleaned_data.get("transaction_type")
        if transaction_type == "I":
            cleaned_data["debit"] = "0.00"

        elif transaction_type == "G":
            cleaned_data["credit"] = "0.00"
        return cleaned_data
