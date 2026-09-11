from django.urls import path

from . import views

from core.views import transition_ecologique, economie_sociale_solidaire, education_citoyenne, mobilisation_communautaire
from core.views import accompagnement, mise_en_reseau, actualites, actualite_detail, rapports_annuels

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

    path(
    "transition-ecologique/",
    transition_ecologique,
    name="transition_ecologique"
    ),

    path(
    "economie-sociale-solidaire/",
    economie_sociale_solidaire,
    name="economie_sociale_solidaire"
    ),

    path(
    "education-citoyenne/",
    education_citoyenne,
    name="education_citoyenne"
    ),

    path(
    "mobilisation-communautaire/",
    mobilisation_communautaire,
    name="mobilisation_communautaire"
    ),

    path(
    "accompagnement/",
    accompagnement,
    name="accompagnement"
    ),

    path(
    "mise-en-reseau/",
    mise_en_reseau,
    name="mise_en_reseau"
    ),

    path(
    "actualites/",
    actualites,
    name="actualites"
    ),

    path(
    "actualites/<slug:slug>/",
    actualite_detail,
    name="actualite_detail"
    ),

    path(
    "rapports-annuels/",
    rapports_annuels,
    name="rapports_annuels"
    ),

    

]

