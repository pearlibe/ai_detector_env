import os
from django.shortcuts import render
from .models import UploadedImage
from .ml_model.nsfw_wrapper import classify_image

def upload_image(request):
    """
    Handles image upload and runs NSFW classification.
    """
    if request.method == 'POST' and request.FILES.get('image'):
        # 1. Save the uploaded image
        img_file = request.FILES['image']
        upload = UploadedImage.objects.create(image=img_file)

        # 2. Build the file system path
        image_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'media',
            upload.image.name
        )

        # 3. Classify the image
        result = classify_image(image_path)
        scores = result[image_path]
        top_label = max(scores, key=scores.get)
        confidence = scores[top_label]

        # 4. Determine offensive status
        offensive_labels = ['porn', 'sexy', 'hentai']
        is_offensive = top_label in offensive_labels and confidence > 0.6

        # 5. Render result page
        context = {
            'uploaded_image': upload,
            'label': top_label,
            'confidence': f"{confidence * 100:.2f}%",
            'is_offensive': is_offensive
        }
        return render(request, 'detector/result.html', context)

    return render(request, 'detector/upload.html')
