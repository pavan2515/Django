from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Course, Registration
from .forms import RegistrationForm

def home(request):
    courses = Course.objects.all()[:6]  # Show latest 6 courses
    total_registrations = Registration.objects.count()
    total_courses = Course.objects.count()
    
    context = {
        'courses': courses,
        'total_registrations': total_registrations,
        'total_courses': total_courses,
    }
    return render(request, 'courses/home.html', context)

def about(request):
    return render(request, 'courses/about.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Registration submitted successfully!')
                return redirect('register')
            except Exception as e:
                messages.error(request, 'Registration failed. You may have already registered for this course.')
    else:
        form = RegistrationForm()
    
    # Get all registrations for display
    registrations = Registration.objects.all()
    
    # Pagination
    paginator = Paginator(registrations, 10)  # Show 10 registrations per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'form': form,
        'registrations': page_obj,
    }
    return render(request, 'courses/register.html', context)

def courses_list(request):
    courses = Course.objects.all()
    context = {
        'courses': courses,
    }
    return render(request, 'courses/courses_list.html', context)