from . import views
from django.urls import path


urlpatterns = [    
    #Film
    path('film-list/', views.filmList, name='film-list'),
    path('film-create', views.filmCreate, name='film-create'),
    path('film-update/<int:id>', views.filmUpdate, name='film-update'),
    path('film-delete/<int:id>', views.filmDelete, name='film-delete'),
    path('film-list/category/<str:category_name>/', views.film_list_by_category, name='film-list-by-category'),
    path('film/<int:film_id>/', views.display_film, name='display-film'),

    #categories
    path('categories/', views.category_list, name='category-list'),
    path('categories/create/', views.category_create, name='category-create'),
    path('categories/update/<int:id>/', views.category_update, name='category-update'),
    path('categories/delete/<int:id>/', views.category_delete, name='category-delete'),
    path('category/<int:category_id>/', views.display_category, name='display-category'),
    
]