# club_app/views.py

from django.shortcuts import render, get_object_or_404
from .models import Member, Club

# Create your views here.

# dashboard/views.py

from django.shortcuts import render

def dashboard1(request):
    return render(request, 'dashboard1/dashboard1.html')

def add_club(request, member_id, club_id):
    member = get_object_or_404(Member, id=member_id)
    club = get_object_or_404(Club, id=club_id)

    # Add the club to the member
    member.clubs.add(club)

    return render(request, 'member_details.html', {'member': member})


def remove_club(request, member_id, club_id):
    member = get_object_or_404(Member, id=member_id)
    club = get_object_or_404(Club, id=club_id)

    # Remove the club from the member
    member.clubs.remove(club)

    return render(request, 'member_details.html', {'member': member})


def update_member_details(request, member_id):
    member = get_object_or_404(Member, id=member_id)

    if request.method == 'POST':
        # Update member details based on form data
        member.first_name = request.POST.get('first_name')
        member.last_name = request.POST.get('last_name')
        member.email = request.POST.get('email')
        # Update other fields as needed
        member.save()

    return render(request, 'member_details.html', {'member': member})


