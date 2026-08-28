from django.db import models

class HomeHero(models.Model):

    title = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )

    subtitle = models.TextField(
        blank=True,
        verbose_name="Description"
    )

    image = models.ImageField(
        upload_to="home/hero/",
        verbose_name="Image"
    )

    button_text = models.CharField(
        max_length=100,
        default="Découvrir nos actions",
        verbose_name="Texte du bouton"
    )

    button_link = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Lien du bouton"
    )

    order = models.PositiveIntegerField(
        default=0,
        verbose_name="Ordre"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )

    class Meta:

        ordering = ["order"]

        verbose_name = "Slide de l'accueil"

        verbose_name_plural = "Slides de l'accueil"


    def __str__(self):

        return self.title
    

class AboutPage(models.Model):

    title = models.CharField(
        max_length=200,
        default="À propos de Com’Unity",
        verbose_name="Titre"
    )

    header_image = models.ImageField(
        upload_to="about/header/",
        verbose_name="Image d'en-tête"
    )

    main_image = models.ImageField(
        upload_to="about/main/",
        verbose_name="Image principale"
    )

    introduction = models.TextField(
        verbose_name="Présentation"
    )

    mission = models.TextField(
        verbose_name="Mission"
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="Actif"
    )


    class Meta:

        verbose_name = "Page À propos"

        verbose_name_plural = "Page À propos"


    def __str__(self):

        return self.title
    

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
