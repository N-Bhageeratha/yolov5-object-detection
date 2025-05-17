import os
from flask import Flask, render_template, request
from pathlib import Path
import torch
import uuid
from PIL import Image
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'static/outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load pretrained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = f"{uuid.uuid4()}.jpg"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)

            results = model(filepath)
            results.render()  # Draw boxes and labels

            # Convert rendered image to PIL format and save
            rendered_img = Image.fromarray(results.ims[0])  # Convert numpy array to PIL
            output_path = os.path.join(OUTPUT_FOLDER, filename)
            rendered_img.save(output_path)

            return render_template('index.html', output_image=output_path)

    return render_template('index.html', output_image=None)

if __name__ == '__main__':
    app.run(debug=True)
