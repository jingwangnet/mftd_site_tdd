from django import forms
from .models import Quote


class QuoteForm(forms.ModelForm):
    required_css_class = "required"

    class Meta:
        model = Quote
        fields = [
            "name",
            "position",
            "company",
            "address",
            "phone",
            "email",
            "web",
            "description",
            "sitestatus",
            "priority",
            "jobfile",
            "quotedate",
            "quoteprice",
        ]
        widgets = {
            "quotedate": forms.SelectDateWidget(),
        }
