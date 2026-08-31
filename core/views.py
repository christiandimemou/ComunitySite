from django.shortcuts import render

from .models import HomeImage, AboutImage, TeamMember


def home(request):

    home_image = HomeImage.objects.filter(
        is_active=True
    ).first()

    return render(
        request,
        "home.html",
        {
            "home_image": home_image,
        }
    )


def about(request):

    about_header_image = AboutImage.objects.filter(
        image_type="header",
        is_active=True
    ).first()

    about_main_image = AboutImage.objects.filter(
        image_type="main",
        is_active=True
    ).first()

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    return render(
        request,
        "about.html",
        {
            "about_header_image": about_header_image,
            "about_main_image": about_main_image,
            "team_members": team_members,
        }
    )