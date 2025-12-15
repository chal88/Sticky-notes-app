""""URL configurations for the notes app."""
from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path("", views.note_list, name="list"),
    path("create/", views.note_create, name="create"),

    # Detail
    path("<int:pk>/", views.note_detail, name="note_detail"),

    # Update (support BOTH names)
    path("<int:pk>/update/", views.note_update, name="note_update"),
    path("<int:pk>/edit/", views.note_update, name="update"),

    # Delete (support BOTH names)
    path("<int:pk>/delete/", views.note_delete, name="note_delete"),
    path("<int:pk>/remove/", views.note_delete, name="delete"),
]
