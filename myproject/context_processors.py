from functools import wraps
from django.http import HttpResponseForbidden
from django.contrib.auth.models import Group
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.http import HttpResponse


def group_required(groups):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            try:
                    user_groups = request.user.groups.values_list('name', flat=True)
            except AttributeError:
                messages.error(request, "User object does not have groups attribute.")
                return redirect('pettycash:home')  # Redirect to a suitable URL
                    
            if any(group in user_groups for group in groups):
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, "Not authorised to view this page.", extra_tags='danger')
                return redirect('pettycash:home')  # Redirect to a suitable URL
        return wrapper
    return decorator

def custom_context(request):
    return {
        'group_required': group_required,
    }