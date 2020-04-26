from django import forms
from django.forms.utils import flatatt
from django.template import Context, Template
from django.utils.safestring import mark_safe


class AceWidget(forms.Textarea):
    def __init__(
        self,
        mode=None,
        theme=None,
        use_worker=True,
        wrap_mode=False,
        width="500px",
        height="300px",
        min_lines=None,
        max_lines=None,
        show_print_margin=True,
        show_invisibles=False,
        use_soft_tabs=True,
        tab_size=None,
        font_size=None,
        toolbar=True,
        *args,
        **kwargs
    ):
        self.mode = mode
        self.theme = theme
        self.use_worker = use_worker
        self.wrap_mode = wrap_mode
        self.width = width
        self.height = height
        self.min_lines = min_lines
        self.max_lines = max_lines
        self.show_print_margin = show_print_margin
        self.show_invisibles = show_invisibles
        self.tab_size = tab_size
        self.font_size = font_size
        self.toolbar = toolbar
        self.use_soft_tabs = use_soft_tabs
        super().__init__(*args, **kwargs)

    @property
    def media(self):
        js = ["django_ace/ace/ace.js", "django_ace/widget.js"]

        if self.mode:
            js.append("django_ace/ace/mode-%s.js" % self.mode)
        if self.theme:
            js.append("django_ace/ace/theme-%s.js" % self.theme)

        css = {"screen": ["django_ace/widget.css"]}

        return forms.Media(js=js, css=css)

    def get_attributes(self):
        ace_attrs = {
            "class": "django-ace-widget loading",
            "style": f"width:{self.width}; height:{self.height}",
            "data-use-worker": self.use_worker,
            "data-show-invisibles": self.show_invisibles,
            "data-show-print-margin": self.show_print_margin,
            "data-use-soft-tabs": self.use_soft_tabs,
            "data-wrap-mode": self.wrap_mode,
        }

        if self.mode:
            ace_attrs["data-mode"] = self.mode
        if self.theme:
            ace_attrs["data-theme"] = self.theme
        if self.min_lines:
            ace_attrs["data-min-lines"] = str(self.min_lines)
        if self.max_lines:
            ace_attrs["data-max-lines"] = str(self.max_lines)
        if self.tab_size:
            ace_attrs["data-tab-size"] = str(self.tab_size)
        if self.font_size:
            ace_attrs["data-font-size"] = str(self.font_size)

        return ace_attrs

    def render(self, name, value, attrs=None, renderer=None):
        textarea = super().render(name, value, attrs, renderer)

        template = Template(
            '{% spaceless %}'
            '<div class="django-ace-editor">'
            '{% if toolbar %}<div style="width: {{ width }}" class="django-ace-toolbar">'
            '<a href="./" class="django-ace-max_min"></a>'
            "</div>{% endif %}"
            '<div{{ ace_attrs }}><div></div></div>{{ textarea|safe }}'
            '</div>'
            '{% endspaceless %}'
        )
        html = template.render(Context({
            'ace_attrs': flatatt(self.get_attributes()),
            'textarea': textarea,
            'toolbar': self.toolbar,
            'width': self.width,
        }))
        return mark_safe(html)
