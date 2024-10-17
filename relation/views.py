from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from relation.models import Relation

@login_required
def follow_user(request, id):
    user_to_follow = get_object_or_404(User, id=id)
    Relation.objects.get_or_create(follower=request.user, following=user_to_follow)
    return redirect('profile', id=id)

@login_required
def unfollow_user(request, id):
    user_to_unfollow = get_object_or_404(User, id=id)
    Relation.objects.filter(follower=request.user, following=user_to_unfollow).delete()
    return redirect('profile', id=id)
