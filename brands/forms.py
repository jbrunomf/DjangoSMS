from django import forms

from brands import models


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ["brand_name", "description", ]
        labels = {"brand_name": "Nome", "description": "Descrição"}
        widgets = {
            "brand_name": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", 'rows': 5}),
        }
