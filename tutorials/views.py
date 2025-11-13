from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tutorial, Progress, Rating
from django.utils import timezone

def tutorial_list(request):
    """Display list of tutorials"""
    tutorials = Tutorial.objects.all()
    
    # Filter by difficulty if provided
    difficulty = request.GET.get('difficulty')
    if difficulty:
        tutorials = tutorials.filter(difficulty=difficulty)
    
    # Filter by category if provided
    category = request.GET.get('category')
    if category:
        tutorials = tutorials.filter(category__icontains=category)
    
    context = {
        'tutorials': tutorials,
    }
    return render(request, 'tutorials/tutorial_list.html', context)


@login_required
def tutorial_detail(request, tutorial_id):
    """Display tutorial details"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    
    # Check if user has progress on this tutorial
    progress = Progress.objects.filter(
        user=request.user,
        tutorial=tutorial
    ).first()
    
    context = {
        'tutorial': tutorial,
        'progress': progress,
    }
    return render(request, 'tutorials/tutorial_detail.html', context)


@login_required
def mark_complete(request, tutorial_id):
    """Mark tutorial as completed"""
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    
    progress, created = Progress.objects.get_or_create(
        user=request.user,
        tutorial=tutorial
    )
    
    progress.completed = True
    progress.completion_date = timezone.now()
    progress.save()
    
    messages.success(request, f'Congratulations! You completed "{tutorial.title}"!')
    return redirect('tutorial_detail', tutorial_id=tutorial_id)


@login_required
def my_progress(request):
    """Display user's learning progress"""
    progress_records = Progress.objects.filter(user=request.user)
    
    completed_count = progress_records.filter(completed=True).count()
    in_progress_count = progress_records.filter(completed=False).count()
    total_time = sum([p.time_spent for p in progress_records])
    
    context = {
        'progress_records': progress_records,
        'completed_count': completed_count,
        'in_progress_count': in_progress_count,
        'total_time': total_time,
    }
    return render(request, 'tutorials/my_progress.html', context)
