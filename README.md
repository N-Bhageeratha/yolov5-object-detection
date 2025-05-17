# 🎯 YOLOv5 Object Detection Web App

This is a web-based object detection system built using **YOLOv5** and **Flask**. The application allows users to upload images, run object detection on them using a pretrained YOLOv5 model (`yolov5s.pt`), and view/download the annotated output.

---

## 📁 Project Structure

```
internship-project/
├── app.py                   # Main Flask backend
├── yolov5/                  # YOLOv5 model directory
├── yolov5s.pt               # Pretrained YOLOv5 weights
├── uploads/                 # Uploaded input images
├── static/
│   └── outputs/             # Output images with detections
├── templates/
│   └── index.html           # Frontend UI
```

---

## 🚀 Features

- Upload any image via web interface
- Perform real-time object detection using YOLOv5
- Display and download results instantly
- Clean and simple HTML frontend using Flask & Jinja2

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/yolov5-object-detection.git
cd yolov5-object-detection
```

### 2. Install Dependencies

```bash
pip install -r yolov5/requirements.txt
pip install flask
```

### 3. Run the Web App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app.

---

## 📷 Demo

| Upload Image | Detected Output |
|--------------|------------------|
| ![upload](static/sample_input.jpg) | ![output](static/outputs/sample_output.jpg) |

---

## 📦 Model Info

- Model used: **YOLOv5s**
- Framework: **PyTorch**
- Source: [ultralytics/yolov5](https://github.com/ultralytics/yolov5)

---

## 📌 Notes

- Make sure your system has GPU support for faster inference (optional).
- You can replace `yolov5s.pt` with any other YOLOv5 variant.

---

