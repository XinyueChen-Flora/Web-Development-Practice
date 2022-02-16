from attr import fields
from django.contrib import admin

# Register your models here.
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_data", "question_text"]

admin.site.register(Question, QuestionAdmin)