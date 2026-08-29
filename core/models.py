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

    def __str__(self):
        return "Image Accueil"

    class Meta:
        verbose_name = "Image de l'accueil"
        verbose_name_plural = "Image de l'accueil"


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
