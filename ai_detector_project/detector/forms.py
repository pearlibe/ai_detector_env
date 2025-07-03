from django import forms
from .models import UploadedImage

class ImageUploadForm(forms.ModelForm):
    """
    Simple form to handle image uploads.
    """
    class Meta:
        model = UploadedImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'image/*'})
        }
        labels = {
            'image': 'Select an Image'
        }
