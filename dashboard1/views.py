from django.shortcuts import render, get_object_or_404, redirect
from .models import Member, Club
from .forms import ClubForm, MemberForm, EventForm, AttendanceForm

# Create your views here.

def dashboard1(request):
    return render(request, 'dashboard1/dashboard1.html')

def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = ClubForm()

    context = {'form': form}
    return render(request, 'dashboard/add_club.html', context)

def add_event(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = EventForm()

    context = {'form': form}
    return render(request, 'dashboard/add_club.html', context)

def add_member(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = MemberForm()

    context = {'form': form}
    return render(request, 'dashboard/add_club.html', context)

def add_attendance(request):
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard_home')
    else:
        form = AttendanceForm()

    context = {'form': form}
    return render(request, 'dashboard/add_club.html', context)


# def add_club(request, member_id, club_id):
#     member = get_object_or_404(Member, id=member_id)
#     club = get_object_or_404(Club, id=club_id)

#     # Add the club to the member
#     member.clubs.add(club)

#     return render(request, 'member_details.html', {'member': member})


# def remove_club(request, member_id, club_id):
#     member = get_object_or_404(Member, id=member_id)
#     club = get_object_or_404(Club, id=club_id)

#     # Remove the club from the member
#     member.clubs.remove(club)

#     return render(request, 'member_details.html', {'member': member})


# def update_member_details(request, member_id):
#     member = get_object_or_404(Member, id=member_id)

#     if request.method == 'POST':
#         # Update member details based on form data
#         member.first_name = request.POST.get('first_name')
#         member.last_name = request.POST.get('last_name')
#         member.email = request.POST.get('email')
#         # Update other fields as needed
#         member.save()

#     return render(request, 'member_details.html', {'member': member})


