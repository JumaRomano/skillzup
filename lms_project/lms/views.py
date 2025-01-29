from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Course, Grade
from .forms import GradeForm

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'lms/admin_dashboard.html')
    elif request.user.role == 'teacher':
        return render(request, 'lms/teacher_dashboard.html')
    elif request.user.role == 'student':
        return render(request, 'lms/student_dashboard.html')

@login_required
def manage_grades(request):
    if request.user.role != 'teacher':
        return redirect('dashboard')

    grades = Grade.objects.all()
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_grades')
    else:
        form = GradeForm()

    return render(request, 'lms/manage_grades.html', {'form': form, 'grades': grades})
