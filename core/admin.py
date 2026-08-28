from django.contrib import admin

from .models import HomeHero, AboutPage, TeamMember

@admin.register(HomeHero)
class HomeHeroAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "order",
        "is_active",
    )

    list_editable = (
        "order",
        "is_active",
    )

    ordering = (
        "order",
    )


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):

    list_display = (
        "title",
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
