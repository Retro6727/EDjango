from functools import wraps
from django.http import HttpResponseForbidden

def superuser_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('login_details')
        if not request.user.is_superuser:
            return HttpResponseForbidden("You are not authorized to view this page")
        return view_func(request, *args, **kwargs)
    return wrapper