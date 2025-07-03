import os
from nsfw_detector import predict

# Adjust path if you saved under a 'pretrained' subfolder
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    'saved_model.h5'
)

# Load the model once at startup
model = predict.load_model(MODEL_PATH)

def classify_image(image_path):
    """
    Returns a dict: { image_path: { label: probability, … } }
    """
    return predict.classify(model, image_path)
