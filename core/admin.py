from django.contrib import admin

from .models import HomeImage, AboutImage, TeamMember, Project, ProjectHeaderImage, Service, ActionPageImage

from .models import GalleryImage, VolunteerApplication, VolunteerHeaderImage, ContactHeaderImage, DonationHeaderImage

from .models import Actualite, ActualiteHeaderImage, RapportAnnuel, RapportHeaderImage


@admin.register(HomeImage)
class HomeImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
    )

    list_editable = (
        "is_active",
    )


@admin.register(AboutImage)
class AboutImageAdmin(admin.ModelAdmin):

    list_display = (
        "image_type",
        "image",
        "is_active",
    )

    list_filter = (
        "image_type",
        "is_active",
    )

    list_editable = (
        "is_active",
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "role",
        "position",
        "order",
        "is_active",
    )

    list_filter = (
        "role",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    ordering = (
        "order",
    )


@admin.register(ProjectHeaderImage)
class ProjectHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "location",
        "order",
        "is_active",
    )

    list_filter = (
        "category",
        "status",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "location",
    )

    list_editable = (
        "status",
        "order",
        "is_active",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
        "-created_at",
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "order",
    )

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "order",
        "is_active",
        "created_at",
    )

    list_filter = (
        "category",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "order",
        "is_active",
    )

    ordering = (
        "order",
        "-created_at",
    )

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "email",
        "domain",
        "status",
        "created_at",
    )

    list_filter = (
        "domain",
        "status",
        "created_at",
    )

    search_fields = (
        "first_name",
        "last_name",
        "email",
        "phone",
        "message",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "created_at",
    )

@admin.register(VolunteerHeaderImage)
class VolunteerHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "-created_at",
    )

@admin.register(ContactHeaderImage)
class ContactHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "-created_at",
    )

@admin.register(DonationHeaderImage)
class DonationHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

    ordering = (
        "-created_at",
    )

@admin.register(ActionPageImage)
class ActionPageImageAdmin(admin.ModelAdmin):

    list_display = (
        "action",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "action",
        "is_active",
    )

    search_fields = (
        "action",
    )

@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "publication_date",
        "is_featured",
        "is_active",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
    )

    search_fields = (
        "title",
        "short_description",
        "content",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    ordering = (
        "-publication_date",
    )

@admin.register(ActualiteHeaderImage)
class ActualiteHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )


@admin.register(RapportAnnuel)
class RapportAnnuelAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "year",
        "is_active",
        "created_at",
    )

    list_filter = (
        "year",
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "-year",
    )

@admin.register(RapportHeaderImage)
class RapportHeaderImageAdmin(admin.ModelAdmin):

    list_display = (
        "image",
        "is_active",
        "created_at",
    )

    list_filter = (
        "is_active",
    )

