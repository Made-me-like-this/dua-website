
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category, Dua, Question

def index(request):
    categories = Category.objects.all()[:5]
    featured_duas = Dua.objects.all()[:3]
    context = {
        'categories': categories,
        'featured_duas': featured_duas,
    }
    return render(request, 'myapp/index.html', context)

def categories(request):
    categories = Category.objects.all()
    return render(request, 'myapp/categories.html', {'categories': categories})

def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    duas = category.duas.all()
    context = {
        'category': category,
        'duas': duas,
    }
    return render(request, 'myapp/category_detail.html', context)

def dua_detail(request, dua_id):
    dua = get_object_or_404(Dua, pk=dua_id)
    return render(request, 'myapp/dua_detail.html', {'dua': dua})

def learn(request):

    return render(request, 'myapp/learn.html')


def questionaires(request):
    questions = Question.objects.all().order_by('-created_at')

    if request.method == 'POST':
        if 'question_submit' in request.POST:
            Question.objects.create(
                title=request.POST.get('title'),
                content=request.POST.get('content'),
                author=request.POST.get('author', 'Anonymous')
            )
        elif 'answer_submit' in request.POST:
            question = Question.objects.get(id=request.POST.get('question_id'))
            new_answer = f"{request.POST.get('author', 'Anonymous')}: {request.POST.get('answer')}\n"
            question.answers = question.answers + new_answer
            question.save()
    return render(request, 'myapp/q$a.html', {'questions': questions})

def about(request):
    return render(request, 'myapp/about.html')

def donate(request):
    return render(request, 'myapp/donate.html')
