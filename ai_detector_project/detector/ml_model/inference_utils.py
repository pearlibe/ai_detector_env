import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os

class OffensiveImageClassifier:
    def __init__(self, model_path, device=None):
        # Determine device (GPU if available, else CPU)
        self.device = device or (torch.device('cuda:0') if torch.cuda.is_available() else torch.device('cpu'))

        # Load the same model architecture & load saved weights
        self.model = models.resnet18(pretrained=False)
        num_features = self.model.fc.in_features
        self.model.fc = nn.Linear(num_features, 2)  # 2 classes
        self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.to(self.device)
        self.model.eval()

        # Preprocessing transforms (must match training)
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                                 [0.229, 0.224, 0.225])
        ])

        # Classes in correct order
        self.class_names = ['non_offensive', 'offensive']

    def predict(self, image_path):
        """
        Returns (label, confidence) for a single image at image_path.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"{image_path} not found.")

        # Load & preprocess image
        image = Image.open(image_path).convert('RGB')
        input_tensor = self.transform(image).unsqueeze(0).to(self.device)  # add batch dim

        # Forward pass
        with torch.no_grad():
            outputs = self.model(input_tensor)
            probabilities = torch.softmax(outputs, dim=1)
            confidence, pred_idx = torch.max(probabilities, dim=1)
            label = self.class_names[pred_idx.item()]
            confidence_score = confidence.item()

        return label, confidence_score
