from django.utils import timezone
from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    # joined_date = models.DateField(auto_now_add=True)
    joined_date = models.DateField(default=timezone.now)
    clubs = models.ManyToManyField(Club, related_name='members')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    attendance_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Attendance(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.member} at {self.event}"
