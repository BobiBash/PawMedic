from django import forms
from django.core.exceptions import ValidationError

from common.models import ReportedIssues


class ReportIssueForm(forms.ModelForm):

    class Meta:
        model = ReportedIssues
        fields = ["title", "issue"]

        widgets = {
            'title': forms.TextInput(attrs={
                "class": 'border rounded-sm px-1 py-2 focus:outline-none w-sm'
            }),
            'issue': forms.Textarea(attrs={
                "class": 'border rounded-sm px-1 py-2 focus:outline-none w-sm',
                "cols": 40,
                "rows": 8,
                "style": 'resize:none',
            })
        }

        error_messages = {
            'title': {
                'required': "This field is required."
            },
            'issue': {
                'required': "This field is required."
            }
        }