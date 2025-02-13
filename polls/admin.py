from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  
    model = Choice  
    extra = 2  

class QuestionAdmin(admin.ModelAdmin):  
    list_display = ('question_text', 'total_votes','has_votes')  

    def total_votes(self, obj):
        return obj.total_votes()
    
    total_votes.short_description = _("Total de Votos")  

    def has_votes(self, obj):
        return obj.has_votes()
    
    has_votes.short_description = _("Contém votos?")

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)