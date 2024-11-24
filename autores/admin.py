from django.contrib import admin
from .models import autores

# Register your models here.

class ExibeAutores(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nacionalidade')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_filter = ('nacionalidade',)
    list_per_page = 2

admin.site.register(autores, ExibeAutores)

