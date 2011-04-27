from django.db import models

class Book(models.Model):
    """(Book description)"""
    title = models.CharField(blank=True, max_length=100)
    author = models.CharField(blank=True, max_length=100)
    cover = models.ImageField(upload_to="covers")

    def image(self):
        if self.cover:
            return '<img src="%s" alt="%s" />' % (self.cover.url, self.title)

    def __unicode__(self):
        return self.title

