from django.db import models



class TODO(models.Model):
    status_choices = [
    ('OP', 'OPEN'),
    ('WR', 'WORKING'),
    ('DN', 'DONE'),
    ('PD', 'PENDING'),
    ]
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=2 , choices=status_choices)
    date = models.DateField()

