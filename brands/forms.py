from django import forms

from brands import models


class BrandForm(forms.ModelForm):
    class Meta:
        model = models.Brand
        fields = ['brand_name', 'description']
