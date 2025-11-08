from django.shortcuts import render, redirect
from django.utils import timezone
from .models import TimeEntry

def toggle_timer(request):
    """Start or stop time tracking with a single button."""
    active = TimeEntry.objects.filter(end_time__isnull=True).first()

    if active:
        # Stop the current timer
        active.end_time = timezone.now()
        active.save()
    else:
        # Start a new timer
        TimeEntry.objects.create(start_time=timezone.now())

    return redirect("timer_view")

def timer_view(request):
    """Displays the timer state with a start/stop button."""
    active = TimeEntry.objects.filter(end_time__isnull=True).first()
    return render(request, "tracker/timer.html", {"active": active})

def history_view(request):
    """Displays all recorded time entries."""
    entries = TimeEntry.objects.all().order_by("-start_time")
    return render(request, "tracker/history.html", {"entries": entries})

