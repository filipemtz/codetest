
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .course import Course


class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Returns the URL to access a detail record ."""
        return reverse('section', args=[str(self.id)])
