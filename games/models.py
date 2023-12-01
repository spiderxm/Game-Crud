import uuid

from django.db import models


class Game(models.Model):
    """
    Game model
    This model will be used to store games information which are present on SVG Platform
    """
    id = models.CharField(max_length=256, default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=256, null=False, blank=False)
    url = models.URLField(null=False)
    author = models.CharField(max_length=256, null=False, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
