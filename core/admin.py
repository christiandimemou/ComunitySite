from django.contrib import admin

from .models import HomeImage, AboutImage, TeamMember


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
