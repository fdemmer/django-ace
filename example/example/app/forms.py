from django import forms

from django_ace import AceWidget
from .models import Snippet


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        widgets = {
            'text': AceWidget(
                mode='html', theme='twilight',
                wrap_mode=True, show_invisibles=True, use_soft_tabs=False,
                tab_size=2, font_size='12pt',
            ),
        }
        exclude = ()
