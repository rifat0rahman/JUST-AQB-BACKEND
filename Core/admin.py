from django.contrib import admin

from django.utils.html import format_html
from .models import CreatePdf

# Register your models here.
class CreatePdfAdmin(admin.ModelAdmin):
    list_display = ('course_title','preview_pdf', 'dept', 'session','is_approved','time')

    def preview_pdf(self, obj):
        if obj.pdf:
            return format_html('<a class="button" target="_blank" href="https://docs.google.com/gview?embedded=true&url={}">Preview PDF</a>',obj.pdf)
        return "No PDF"
    
    preview_pdf.short_description = "Preview PDF"
    preview_pdf.allow_tags = True


admin.site.register(CreatePdf, CreatePdfAdmin)