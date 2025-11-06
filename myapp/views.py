from django.shortcuts import render


def portfolio(request):
    skills = ['Python', 'HTML', 'CSS', 'React']
    projects = [
        {'name': 'Portfolio Website', 'desc': 'Built with Django', 'tech': 'Python, HTML, CSS'},
        {'name': 'Todo App', 'desc': 'React frontend', 'tech': 'React'},
        {'name': 'Weather Dashboard', 'desc': 'Uses API integration', 'tech': 'Python'},
        {'name': 'Responsive Calculator', 'desc': 'Built with Django templates', 'tech': 'HTML, CSS, Django'}
    ]
    return render(request, 'myapp/portfolio.html', {'skills': skills, 'projects': projects})

def products(request):
    products = [
        {'name': 'Smartwatch', 'price': 2499, 'image': 'watch.jpg', 'category': 'Gadgets', 'sale': True},
        {'name': 'Wireless Earbuds', 'price': 1599, 'image': 'earbuds.jpg', 'category': 'Gadgets', 'sale': False},
        {'name': 'Cotton Shirt', 'price': 799, 'image': 'shirt.jpg', 'category': 'Clothing', 'sale': True},
        {'name': 'Sneakers', 'price': 2199, 'image': 'sneakers.jpg', 'category': 'Clothing', 'sale': False},
    ]
    return render(request, 'myapp/products.html', {'products': products})

def student(request):
    student = {'name': 'Kalyani', 'marks': [85, 92, 76, 60, 45]}
    return render(request, 'myapp/student.html', {'student': student})

def calculator(request):
    return render(request, 'myapp/calculator.html')
