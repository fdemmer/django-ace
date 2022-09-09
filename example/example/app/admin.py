from django.contrib import admin
from django.db import models

from django_ace import AceWidget

from .models import Snippet, SnippetGroup

default_ace_widget = AceWidget(mode='html', theme='textmate')


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': default_ace_widget},
        models.JSONField: {'widget': AceWidget(mode='json', theme='textmate')},
    }


class SnippetInline(admin.TabularInline):
    model = Snippet
    formfield_overrides = {
        models.TextField: {'widget': default_ace_widget},
    }


@admin.register(SnippetGroup)
class SnippetGroupAdmin(admin.ModelAdmin):
    inlines = [SnippetInline]
