from django.db import models

class HomeImage(models.Model):

    image = models.ImageField(
        upload_to="home/",
        verbose_name="Image"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Image active"
    )

    class Meta:
        verbose_name = "Image de l'accueil"
        verbose_name_plural = "Image de l'accueil"

    def __str__(self):
        return "Image Accueil"


class AboutImage(models.Model):

    IMAGE_TYPES = [
        ("header", "Image en-tête"),
        ("main", "Image principale"),
    ]

    image_type = models.CharField(
        max_length=20,
        choices=IMAGE_TYPES,
        verbose_name="Type d'image"
    )

    image = models.ImageField(
        upload_to="about/",
        verbose_name="Image"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Image active"
    )

    class Meta:
        verbose_name = "Image de la page À propos"
        verbose_name_plural = "Images de la page À propos"

    def __str__(self):
        return self.get_image_type_display()
    

class TeamMember(models.Model):

    ROLE_CHOICES = [

        ("founder", "Fondateur"),

        ("member", "Membre"),

    ]


    name = models.CharField(
        max_length=150,
        verbose_name="Nom complet"
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="member",
        verbose_name="Rôle"
    )

    position = models.CharField(
        max_length=200,
        verbose_name="Poste / Fonction"
    )

    description = models.TextField(
        verbose_name="Description"
    )

    photo = models.ImageField(
        upload_to="about/team/",
        verbose_name="Photo"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Afficher sur le site"
    )


    class Meta:

        ordering = ["order"]

        verbose_name = "Membre de l'équipe"

        verbose_name_plural = "Membres de l'équipe"


    def __str__(self):

        return self.name


class Project(models.Model):

    CATEGORY_CHOICES = [
        ("ecologie", "Transition écologique"),
        ("ess", "Économie sociale et solidaire"),
        ("citoyennete", "Éducation citoyenne"),
    ]

    STATUS_CHOICES = [
        ("ongoing", "En cours"),
        ("completed", "Terminé"),
        ("upcoming", "À venir"),
    ]

    title = models.CharField(
        max_length=200,
        verbose_name="Titre du projet"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        verbose_name="Catégorie"
    )

    short_description = models.CharField(
        max_length=300,
        verbose_name="Description courte"
    )

    description = models.TextField(
        verbose_name="Description complète"
    )

    image = models.ImageField(
        upload_to="projects/",
        verbose_name="Image du projet"
    )

    location = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Lieu"
    )

    project_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Date"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ongoing",
        verbose_name="Statut"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Afficher sur le site"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "-created_at"]
        verbose_name = "Projet"
        verbose_name_plural = "Projets"

    def __str__(self):
        return self.title
    

class ProjectHeaderImage(models.Model):
    image = models.ImageField(
        upload_to="projects/",
        verbose_name="Image d'en-tête"
    )

    class Meta:
        verbose_name = "Image d'en-tête des projets"
        verbose_name_plural = "Image d'en-tête des projets"

    def __str__(self):
        return "Image d'en-tête - Projets"


class Service(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="Nom du service"
    )

    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"
    )

    short_description = models.CharField(
        max_length=300,
        verbose_name="Description courte"
    )

    description = models.TextField(
        verbose_name="Description détaillée"
    )

    image = models.ImageField(
        upload_to="services/",
        verbose_name="Image"
    )

    icon = models.CharField(
        max_length=50,
        default="fa-leaf",
        verbose_name="Icône Font Awesome"
    )

    interventions = models.TextField(
        blank=True,
        verbose_name="Domaines d'intervention",
        help_text="Séparer les éléments par une virgule."
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre d'affichage"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Service actif"
    )

    class Meta:
        ordering = ["order"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title
    
    @property
    def intervention_list(self):
        return [
            intervention.strip()
            for intervention in self.interventions.split(",")
            if intervention.strip()
        ]