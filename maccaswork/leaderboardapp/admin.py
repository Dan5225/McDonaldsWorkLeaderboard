
from django.contrib import admin
from .models import Firstname, Lastname, Fullname, Tehs


@admin.register(Firstname)
class FirstnameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name_text')
    search_fields = ('first_name_text',)


@admin.register(Lastname)
class LastnameAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name_text')
    search_fields = ('last_name_text',)


@admin.register(Fullname)
class FullnameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name')
    search_fields = ('first_name__first_name_text', 'last_name__last_name_text')


@admin.register(Tehs)
class TehsAdmin(admin.ModelAdmin):
    list_display = ('id', 'participant', 'tehs')
    search_fields = (
        'participant__first_name__first_name_text',
        'participant__last_name__last_name_text',
    )
    ordering = ('-tehs',)
