from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'emailid', 'mobile', 'team', 'position')
    list_filter = ('team', 'position', 'gender', 'agecategory')
    search_fields = ('firstname', 'lastname', 'emailid', 'team__title')

    fieldsets = (
        ('Personal Information', {
            'fields': ('firstname', 'lastname', 'profile', 'nationality', 'dateofbirth', 'gender', 'aadhar', 'aadhar_photo', 'emailid', 'mobile', 'address', 'state', 'district', 'pincode')
        }),
        ('Physical Details', {
            'fields': ('weight', 'height')
        }),
        ('Guardian Information', {
            'fields': ('guardian_name', 'relation', 'guardiancontact')
        }),
        ('Player Details', {
            'fields': ('agecategory', 'team', 'position', 'role', 'handiness')
        }),
        ('Medical History', {
            'fields': ('disease', 'allergies', 'additional_information')
        }),
    )

    readonly_fields = ('profile_preview', 'aadhar_photo_preview')

    def profile_preview(self, obj):
        return obj.profile_preview

    profile_preview.short_description = 'Profile Preview'
    profile_preview.allow_tags = True

    def aadhar_photo_preview(self, obj):
        return obj.aadhar_photo_preview

    aadhar_photo_preview.short_description = 'Aadhar Photo Preview'
    aadhar_photo_preview.allow_tags = True

class ChoiceInline(admin.TabularInline):
    model = Multiple_choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'question_type', 'form')
    list_filter = ('question_type', 'form')
    search_fields = ('question_text',)
    inlines = [ChoiceInline]

class FormAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('form', 'created_at')
    list_filter = ('form',)
    search_fields = ('form__title',)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('response', 'question', 'answer_text', 'file_upload', 'date', 'time')
    list_filter = ('response', 'question')
    search_fields = ('response__form__title', 'question__question_text', 'answer_text')


@admin.register(Multiple_choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')
    search_fields = ('choice_text',)

admin.site.register(Form, FormAdmin)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Answer, AnswerAdmin)