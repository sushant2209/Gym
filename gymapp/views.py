from django.shortcuts import get_object_or_404, render,redirect
from .forms import UserProfileForm
from .models import UserProfile
from datetime import datetime, timedelta
from django.db.models import Q
from django.db import models

def home(request):
    return render(request, 'home.html')

def addMember(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/success')  
    else:
        form = UserProfileForm()
    return render(request, 'addMember.html', {'form': form})

def pendingFees(request):
    # Retrieve members whose memberships have ended (membership_end_date is in the past) or membership_end_date is None
    expired_members = UserProfile.objects.filter(
        Q(membership_end_date__lt=datetime.now()) | Q(membership_end_date__isnull=True)
    ).order_by('-membership_end_date')
    
    return render(request, 'pendingFees.html', {'expired_members': expired_members})


def success(request):
    return render(request, 'success.html')



def members(request):
    users = UserProfile.objects.all()
    return render(request, 'members.html', {'members': users})

def addFees(request, member_id):
    if request.method == 'POST':
        membership_duration = int(request.POST.get('membershipDuration'))
        user_profile = UserProfile.objects.get(pk=member_id)
        user_profile.membership_start_date = datetime.now().date()
        if membership_duration == 1:
            user_profile.membership_end_date = user_profile.membership_start_date + timedelta(days=30)
        elif membership_duration == 2:
            user_profile.membership_end_date = user_profile.membership_start_date + timedelta(days=60)
        user_profile.save()
        return redirect('/pendingFees')
    return render(request, 'addFees.html')

def user_profile(request,user_id):
    user = get_object_or_404(UserProfile, pk=user_id)
    return render(request, 'userProfile.html', {'user': user})
