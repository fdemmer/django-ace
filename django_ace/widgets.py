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
        wordwrap=False,
        width='500px',
        height='300px',
        minlines=None,
        maxlines=None,
        showprintmargin=True,
        showinvisibles=False,
        usesofttabs=True,
        tabsize=None,
        fontsize=None,
        toolbar=True,
        readonly=False,
        showgutter=True,
        behaviours=True,
        extensions=None,
        *args,
        **kwargs
    ):
        self.mode = mode
        self.theme = theme
        self.use_worker = use_worker
        self.wordwrap = wordwrap
        self.width = width
        self.height = height
        self.minlines = minlines
        self.maxlines = maxlines
        self.showprintmargin = showprintmargin
        self.showinvisibles = showinvisibles
        self.tabsize = tabsize
        self.fontsize = fontsize
        self.toolbar = toolbar
        self.readonly = readonly
        self.behaviours = behaviours
        self.showgutter = showgutter
        self.usesofttabs = usesofttabs
        self.extensions = extensions
        super().__init__(*args, **kwargs)

    @property
    def media(self):
        js = ['django_ace/ace/ace.js', 'django_ace/widget.js']

        if self.mode:
            js.append('django_ace/ace/mode-%s.js' % self.mode)
        if self.theme:
            js.append('django_ace/ace/theme-%s.js' % self.theme)
        if self.extensions:
            for extension in self.extensions:
                js.append('django_ace/ace/ext-%s.js' % extension)

        css = {'screen': ['django_ace/widget.css']}

        return forms.Media(js=js, css=css)

    def get_attributes(self):
        ace_attrs = {
            'class': 'django-ace-widget loading',
            'style': f'width:{self.width}; height:{self.height}',
            'data-use-worker': self.use_worker,
            'data-showinvisibles': self.showinvisibles,
            'data-showprintmargin': self.showprintmargin,
            'data-usesofttabs': self.usesofttabs,
            'data-wordwrap': self.wordwrap,
        }

        if self.mode:
            ace_attrs['data-mode'] = self.mode
        if self.theme:
            ace_attrs['data-theme'] = self.theme
        if self.minlines:
            ace_attrs['data-minlines'] = str(self.minlines)
        if self.maxlines:
            ace_attrs['data-maxlines'] = str(self.maxlines)
        if self.tabsize:
            ace_attrs['data-tabsize'] = str(self.tabsize)
        if self.fontsize:
            ace_attrs['data-fontsize'] = str(self.fontsize)

        ace_attrs['data-readonly'] = 'true' if self.readonly else 'false'
        ace_attrs['data-showgutter'] = 'true' if self.showgutter else 'false'
        ace_attrs['data-behaviours'] = 'true' if self.behaviours else 'false'

        return ace_attrs

    def render(self, name, value, attrs=None, renderer=None):
        textarea = super().render(name, value, attrs, renderer)

        template = Template(
            '{% spaceless %}'
            '<div class="django-ace-editor">'
            '{% if toolbar %}<div style="width: {{ width }}" class="django-ace-toolbar">'
            '<a href="./" class="django-ace-max_min"></a>'
            '</div>{% endif %}'
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
