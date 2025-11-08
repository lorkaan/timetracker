from django.db import models
from django.utils import timezone

class TimeEntry(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)

    def is_active(self):
        return self.end_time is None

    def duration(self):
        if self.end_time:
            return self.end_time - self.start_time
        return timezone.now() - self.start_time

    def __str__(self):
        if self.end_time:
            return f"Session: {self.start_time} → {self.end_time} ({self.duration()})"
        return f"Session: {self.start_time} → [active]"
