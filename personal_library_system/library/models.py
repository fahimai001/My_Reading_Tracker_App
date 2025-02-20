from django.db import models

class Book(models.Model):
    STATUS_CHOICES = [
        ('reading', 'Reading'),
        ('completed', 'Done'),
        ('not-started', 'Not Started'),
    ]
    BOOK_TYPE_CHOICES = [
        ('TECH', 'Tech Book'),
        ('NOVEL', 'Novel Book'),
    ]

    name = models.CharField(max_length=255)
    date_added = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='not-started')
    book_type = models.CharField(max_length=10, choices=BOOK_TYPE_CHOICES)

    def __str__(self):
        return self.name
