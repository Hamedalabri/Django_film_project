from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Film
from .forms import FilmForm , CategoryForm

def filmList(request):
    films = Film.objects.all()  
    return render(request, "film-list.html", {'films': films})

def display_film(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'display_film.html', {'film': film})

def filmCreate(request):
    if request.method == "POST":
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('film-list')
    else:
        form = FilmForm()
    return render(request, 'film-create.html', {'form': form})

def filmUpdate(request, id):
    film = Film.objects.get( pk=id)
    if request.method == "POST":
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('film-list')
    else:
        form = FilmForm(instance=film)
    return render(request, 'film-update.html', {'form': form})

def filmDelete(request, id):
    film = get_object_or_404(Film, pk=id)
    film.delete()
    return redirect('film-list')

def film_list_by_category(request, category_name):
    category = Category.objects.get(name=category_name)
    films = Film.objects.filter(category=category)
    return render(request, 'film-list.html', {'films': films, 'category': category})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm()
    return render(request, 'category_create.html', {'form': form})

def category_update(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category-list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'category_update.html', {'form': form})

def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return redirect('category-list')

def display_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    films = Film.objects.filter(category=category)
    return render(request, 'display_category.html', {'category': category, 'films': films})


