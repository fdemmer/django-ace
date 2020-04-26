from django.db import models


class SnippetGroup(models.Model):
    name = models.CharField(max_length=64)


class Snippet(models.Model):
    group = models.ForeignKey(
        SnippetGroup,
        on_delete=models.SET_NULL,
        null=True, blank=True,
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at', )
