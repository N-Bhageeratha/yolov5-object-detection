import torch

# Load model directly from GitHub
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', source='github')

# Load your image (make sure the image is in this folder)
img = 'test.jpg'  # Change to your actual image name

# Run inference
results = model(img)

# Show and save results
results.print()
results.show()
results.save()
