from django.shortcuts import render
from .models import TeamMember, AboutPage

def home(request):
    return render(request, "home.html")


def about(request):

    team_members = TeamMember.objects.filter(
        is_active=True
    )

    contenue = AboutPage.objects.filter(
       is_active=True 
    )

    return render(
        request,
        "about.html",
        {
            "team_members": team_members,
        }
    )