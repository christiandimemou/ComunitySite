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
    "projets/<slug:slug>/", 
     views.project_detail, 
     name="project_detail"
     ),

    path(
    "services/",
    views.services,
    name="services"
    ),

    path(
    "services/<slug:slug>/", 
    views.service_detail, 
    name="service_detail"
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

    path(
    "contact/",
    views.contact,
    name="contact"
    ),

    path(
    "faq/", 
    views.faq, 
    name="faq"
    ),

    path(
    "faire-un-don/",
    views.donation,
    name="donation"
    ),

    

]

