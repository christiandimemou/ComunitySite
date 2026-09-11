from django.shortcuts import render, get_object_or_404

from .models import HomeImage, AboutImage, TeamMember, Project, ProjectHeaderImage, Service
from .models import GalleryImage, VolunteerApplication, VolunteerHeaderImage, ContactHeaderImage, DonationHeaderImage
from .forms import ContactForm
from .models import (
    HomeImage,
    AboutImage,
    TeamMember,
    Project,
    ProjectHeaderImage,
    ActionPageImage,
)

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


def service_detail(request, slug):
    service = get_object_or_404(
        Service,
        slug=slug,
        is_active=True
    )

    related_services = Service.objects.filter(
        is_active=True
    ).exclude(
        id=service.id
    ).order_by("order")[:4]

    return render(
        request,
        "service_detail.html",
        {
            "service": service,
            "related_services": related_services,
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


def contact(request):

    contact_header = ContactHeaderImage.objects.filter(
        is_active=True
    ).first()

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            return render(
                request,
                "contact.html",
                {
                    "form": ContactForm(),
                    "contact_header": contact_header,
                    "success": True,
                }
            )

    else:
        form = ContactForm()

    return render(
        request,
        "contact.html",
        {
            "form": form,
            "contact_header": contact_header,
        }
    )


def donation(request):

    donation_header = DonationHeaderImage.objects.filter(
        is_active=True
    ).first()

    return render(
        request,
        "donation.html",
        {
            "donation_header": donation_header,
        }
    )


def project_detail(request, slug):
    project = get_object_or_404(
        Project,
        slug=slug,
        is_active=True
    )

    related_projects = Project.objects.filter(
        is_active=True,
        category=project.category
    ).exclude(
        id=project.id
    )[:3]

    return render(
        request,
        "project_detail.html",
        {
            "project": project,
            "related_projects": related_projects,
        }
    )


def faq(request):
    faq_header = ContactHeaderImage.objects.filter(
        is_active=True
    ).first()

    return render(
        request,
        "faq.html",
        {
            "faq_header": faq_header,
        }
    )


def transition_ecologique(request):

    action_image = ActionPageImage.objects.filter(
        action="transition",
        is_active=True
    ).first()

    return render(
        request,
        "transition_ecologique.html",
        {
            "action_image": action_image,
        }
    )

def economie_sociale_solidaire(request):

    action_image = ActionPageImage.objects.filter(
        action="ess",
        is_active=True
    ).first()

    return render(
        request,
        "economie_sociale_solidaire.html",
        {
            "action_image": action_image,
        }
    )

def education_citoyenne(request):

    action_image = ActionPageImage.objects.filter(
        action="education",
        is_active=True
    ).first()

    return render(
        request,
        "education_citoyenne.html",
        {
            "action_image": action_image,
        }
    )

def mobilisation_communautaire(request):

    action_image = ActionPageImage.objects.filter(
        action="mobilisation",
        is_active=True
    ).first()

    return render(
        request,
        "mobilisation_communautaire.html",
        {
            "action_image": action_image,
        }
    )

def accompagnement(request):

    action_image = ActionPageImage.objects.filter(
        action="accompagnement",
        is_active=True
    ).first()

    return render(
        request,
        "accompagnement.html",
        {
            "action_image": action_image,
        }
    )

