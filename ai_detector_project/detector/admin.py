from django.contrib import admin
from .models import UploadedImage, ClassificationResult

@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at', 'image')
    readonly_fields = ('uploaded_at',)

@admin.register(ClassificationResult)
class ClassificationResultAdmin(admin.ModelAdmin):
    list_display = ('uploaded_image', 'label', 'confidence', 'processed_at')
    readonly_fields = ('processed_at',)
