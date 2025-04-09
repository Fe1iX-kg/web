from django.http import JsonResponse
from django.shortcuts import render

from .models import Student


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def address(request):
    return render(request, 'address.html')

def support(request):
    return render(request, 'support.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    context = {'company_name': 'Моя Компания', 'year': 2025}
    return render(request, 'about.html', context)

def students_list(request):
    students = Student.objects.all()
    data = [{'name': s.name, 'age': s.age, 'email': s.email, 'enrolled': s.enrolled} for s in students]
    return JsonResponse(data, safe=False)

def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        data = {
            'name': student.name,
            'age': student.age,
            'email': student.email,
            'enrolled': student.enrolled
        }
    except Student.DoesNotExist:
        data = {'error': 'Студент не найден'}
    return JsonResponse(data)