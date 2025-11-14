from django.shortcuts import render, get_object_or_404
from .models import Product


def portfolio(request):
    skills = ['Python', 'HTML', 'CSS', 'React']
    projects = [
        {'name': 'Portfolio Website', 'desc': 'Built with Django', 'tech': 'Python, HTML, CSS'},
        {'name': 'Todo App', 'desc': 'React frontend', 'tech': 'React'},
        {'name': 'Weather Dashboard', 'desc': 'Uses API integration', 'tech': 'Python'},
        {'name': 'Responsive Calculator', 'desc': 'Built with Django templates', 'tech': 'HTML, CSS, Django'}
    ]
    return render(request, 'myapp/portfolio.html', {'skills': skills, 'projects': projects})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'myapp/product_detail.html', {'product': product})

def student(request):
    student = {'name': 'Kalyani', 'marks': [85, 92, 76, 60, 45]}
    return render(request, 'myapp/student.html', {'student': student})

def calculator(request):
    return render(request, 'myapp/calculator.html')
