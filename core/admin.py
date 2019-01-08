from django.contrib import admin
from .models import *
# Register your models here.


class TurmaInlineAdmin(admin.TabularInline):
    model = Turma
    extra = 0

    def get_extra(self,request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class CursoAdmin(admin.ModelAdmin):
    inlines = [TurmaInlineAdmin]
    list_display = ('data_festa', 'cliente', 'valor')
    list_filter = ('carga_horaria', 'valor')


class TurmaAdmin(admin.ModelAdmin):
    list_display = ('data_inicio','curso','professor')


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('nome','telefone','valor_hora_aula')
    ordering = ['nome']
    search_fields = ['nome']


admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor,ProfessorAdmin)

#default:"Administração do Django"
admin.site.site_header='Painel de Controle'

#default:"Administração do Site"
admin.site.index_title=''

#default:"Site de Administração do Django"
admin.site.site_title='Questão 02'