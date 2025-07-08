
 🧠 AI-Powered NSFW Image Detector 🌐

A Django-based web application that uses a pre-trained deep learning model to detect offensive (NSFW) content in images. Users can upload images through a web interface and receive predictions in real-time.



 🚀 Features

🔍 Upload and scan images for NSFW content
🤖 Powered by pre-trained MobileNet model for NSFW classification
📦 Built with Django (backend) and HTML/CSS (frontend)
🗂 Simple UI with real-time feedback
💾 Saves upload logs for review
🖼 Handles multiple NSFW classes like porn, sexy, hentai, etc.



📁 Folder Structure

```
ai_detector_env/
├── ai_detector_project/          # Django project folder
├── detector/                     # Django app
│   ├── ml_model/                 # Contains the pre-trained model
│   │   └── nsfw_mobilenet2.224x224.h5
│   ├── templates/
│   │   └── detector/
│   │       ├── upload.html       # Image upload page
│   │       └── result.html       # Prediction result page
├── media/
│   └── uploads/                  # Stores user-uploaded images
├── venv/                         # Virtual environment
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```


🛠 Installation Guide

Clone the Repository or Download ZIP

bash
git clone https://github.com/pearlibe/ai_detector_env.git



2. Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate      For Windows


3. Install Required Packages
pip install django pillow numpy tensorflow keras



 4. Download the Pre-Trained NSFW Model

Download `nsfw_mobilenet2.224x224.h5` from:

🔗 https://github.com/GantMan/nsfw_model/releases

Place it in:

detector/ml_model/save_model.h5 it has been already placed in the destinated folder 



 5. Run Migrations and Start Server

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)



🧪 How It Works

1. User uploads an image via the form.
2. Image is saved in `media/uploads/`.
3. Django sends the image to the prediction engine using the NSFW pre-trained model.
4. Result (e.g., "porn", "sexy", "neutral", etc.) is displayed on `result.html`.




 🙌 Credits

 [GantMan/nsfw_model](https://github.com/GantMan/nsfw_model) — Pretrained NSFW model
TensorFlow / Keras / PyTorch
Django Community

