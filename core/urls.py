from django.urls import path

from . import views


urlpatterns = [

    path("", views.home, name="home"),

    path(
        "a-propos/",
        views.about,
        name="about"
    ),

    path(
    "projets/",
    views.projects,
    name="projects"
    ),

    path(
    "services/",
    views.services,
    name="services"
    ),

    path(
    "galerie/",
    views.gallery,
    name="gallery"
    ),

    path(
    "devenir-benevole/",
    views.volunteer,
    name="volunteer"
    ),

]