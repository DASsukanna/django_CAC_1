# dashboard/forms.py
from django import forms
from .models import Club, Member, Event, Attendance

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['name', 'description']

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'age', 'gender', 'phone_number', 'clubs']
        exclude = ['joined_date']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'location', 'description', 'attendance_limit']

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['member', 'event', 'attended', 'check_in_time', 'check_out_time']
