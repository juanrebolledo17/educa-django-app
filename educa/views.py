from django.shortcuts import redirect

def landing_logic(request):
    if request.user.is_authenticated:
        return redirect('courses:manage_course_list')
    else:
        return redirect('login')