from django.shortcuts import render

from .models import HomeImage, AboutImage, TeamMember, Project, ProjectHeaderImage, Service
from .models import GalleryImage, VolunteerApplication, VolunteerHeaderImage

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


def projects(request):
    projects_list = Project.objects.filter(
        is_active=True
    )

    project_header = ProjectHeaderImage.objects.first()

    return render(
        request,
        "projects.html",
        {
            "projects": projects_list,
            "project_header": project_header,
        }
    )


def services(request):

    services_list = Service.objects.filter(
        is_active=True
    )

    return render(
        request,
        "services.html",
        {
            "services": services_list,
        }
    )


def gallery(request):

    gallery_images = GalleryImage.objects.filter(
        is_active=True
    ).order_by(
        "order",
        "-created_at"
    )

    return render(
        request,
        "gallery.html",
        {
            "gallery_images": gallery_images,
        }
    )

def volunteer(request):

    if request.method == "POST":

        VolunteerApplication.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            domain=request.POST.get("domain"),
            message=request.POST.get("message"),
        )

        return render(
            request,
            "volunteer.html",
            {
                "success": True
            }
        )

    return render(request, "volunteer.html")

def volunteer(request):

    volunteer_header = VolunteerHeaderImage.objects.filter(
        is_active=True
    ).first()

    if request.method == "POST":

        VolunteerApplication.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            domain=request.POST.get("domain"),
            message=request.POST.get("message"),
        )

        return render(
            request,
            "volunteer.html",
            {
                "volunteer_header": volunteer_header,
                "success": True,
            }
        )

    return render(
        request,
        "volunteer.html",
        {
            "volunteer_header": volunteer_header,
        }
    )