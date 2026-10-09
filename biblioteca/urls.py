from django.urls import path

from . import views

urlpatterns = [
    path("libros/", views.libro_list, name="libro-list"),
    path("libros/<int:pk>/", views.libro_detail, name="libro-detail"),
    path("resenas/", views.ResenaListCreate.as_view(), name="resena-list-create"),
    path("resenas/<int:pk>/", views.ResenaRetrieveUpdateDestroy.as_view(), name="resena-detail"),
]
