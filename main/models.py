from django.db import models
import uuid

class Application(models.Model):
    STATUS_CHOICES = [
        (None, 'None'),
        ('submitted', 'Submitted'),  # Changed from 'pending' to 'submitted'
        ('waitlisted', 'Waitlisted'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=True, blank=True)
    private = models.JSONField(default=dict)
    deposit = models.JSONField(default=dict)
    waitlist_position = models.IntegerField(null=True, blank=True)
    application_data = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username} - {self.status}"
