from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import Profile
from .models import MentorshipRequest, PeerGroup, MentorshipSession

def mentor_list(request):
    """Display list of available mentors"""
    mentors = Profile.objects.filter(user_type='mentor')
    
    context = {
        'mentors': mentors,
    }
    return render(request, 'mentorship/mentor_list.html', context)


@login_required
def request_mentor(request, mentor_id):
    """Send mentorship request to a mentor"""
    mentor = get_object_or_404(User, id=mentor_id)
    
    # Check if already requested
    existing_request = MentorshipRequest.objects.filter(
        mentee=request.user,
        mentor=mentor
    ).first()
    
    if existing_request:
        messages.warning(request, 'You have already sent a request to this mentor.')
        return redirect('mentor_list')
    
    if request.method == 'POST':
        message = request.POST.get('message', '')
        MentorshipRequest.objects.create(
            mentee=request.user,
            mentor=mentor,
            message=message
        )
        messages.success(request, f'Mentorship request sent to {mentor.username}!')
        return redirect('mentor_list')
    
    return render(request, 'mentorship/request_mentor.html', {'mentor': mentor})


@login_required
def peer_groups(request):
    """Display list of peer groups"""
    groups = PeerGroup.objects.all()
    
    context = {
        'groups': groups,
    }
    return render(request, 'mentorship/peer_groups.html', context)


@login_required
def join_group(request, group_id):
    """Join a peer group"""
    group = get_object_or_404(PeerGroup, id=group_id)
    
    if request.user in group.members.all():
        messages.info(request, 'You are already a member of this group.')
    else:
        group.members.add(request.user)
        messages.success(request, f'You have joined {group.name}!')
    
    return redirect('peer_groups')


@login_required
def create_group(request):
    """Create a new peer group"""
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        focus_area = request.POST.get('focus_area')
        max_members = request.POST.get('max_members', 20)
        
        group = PeerGroup.objects.create(
            name=name,
            description=description,
            focus_area=focus_area,
            max_members=max_members,
            created_by=request.user
        )
        group.members.add(request.user)
        
        messages.success(request, f'Group "{name}" created successfully!')
        return redirect('peer_groups')
    
    return render(request, 'mentorship/create_group.html')
