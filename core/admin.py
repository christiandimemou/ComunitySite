from django.contrib import admin

from .models import HomeImage, AboutImage, TeamMember, Project, ProjectHeaderImage, Service

from .models import GalleryImage


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

