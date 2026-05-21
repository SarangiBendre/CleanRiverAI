# 🌊 Clean River AI  
### AI-Based Plastic Waste Detection and Pollution Level Classification System

> “Technology becomes meaningful when it creates impact beyond screens.”

Clean River AI is an AI-powered environmental monitoring system developed to detect plastic waste in rivers using Computer Vision and Deep Learning techniques.

The project uses YOLOv8 object detection to analyze river images and automatically classify pollution levels based on detected plastic waste. The system aims to provide a smart and practical solution for environmental monitoring and river cleanliness management.

---

# 📖 Project Overview

River pollution caused by plastic waste has become one of the major environmental concerns worldwide. Traditional river monitoring methods mostly depend on manual inspection, which is time-consuming, costly, and inefficient for continuous monitoring.

Clean River AI provides an automated solution that uses Artificial Intelligence and Computer Vision to detect plastic waste from river images in real-time. The system identifies waste objects, analyzes pollution severity, and generates visual detection results using deep learning algorithms.

This project demonstrates how modern AI technologies can contribute towards environmental sustainability and smarter pollution monitoring systems.

---

## 🚀 Key Features

- AI-powered plastic waste detection
- Real-time pollution level classification
- Image upload and automatic analysis
- Detection result visualization with bounding boxes
- User login and registration system
- Detection history management
- Flask-based web application
- Lightweight and user-friendly interface

---

## ⚙️ System Workflow

1. User uploads a river image through the web application.
2. The image is processed using OpenCV.
3. YOLOv8 model detects plastic waste objects.
4. Detected objects are counted automatically.
5. Pollution level is classified based on waste count.
6. Detection result image is generated and displayed.
7. Detection details are stored in the database for history tracking.

---

## 🛠 Technologies Used

- Python
- Flask
- YOLOv8
- OpenCV
- SQLite
- HTML/CSS
- Deep Learning
- Computer Vision

---

## 🤖 AI Model Information

- Model Used: YOLOv8
- Framework: Ultralytics YOLO
- Detection Type: Object Detection
- Training Method: Transfer Learning
- Dataset Type: Custom River Plastic Waste Dataset

The model was trained using annotated river waste images to improve detection accuracy and real-time performance.

---

## 📊 Pollution Level Classification

| Plastic Waste Count | Pollution Level |
|---------------------|----------------|
| 0                   | Not Polluted |
| 1 – 5               | Low |
| 6 – 15              | Medium |
| Above 15            | High |

---

## 📂 Project Structure

```bash
CleanRiverAI/
│
├── app.py
├── database.py
├── requirements.txt
├── model/
│   └── best.pt
├── static/
├── templates/
└── database.db
```

---

## 🎥 Demo Video

🔗 https://youtu.be/PK22Fx0rTvo

---

## 🎯 Future Improvements

- Live CCTV monitoring
- Drone-based river monitoring
- Mobile application integration
- Real-time pollution alerts
- Government dashboard integration
- Cloud-based environmental monitoring
- Multi-class waste detection system

---

## 👩‍💻 Project Team

- Sarangi Bendre *(Team Leader)*
- Harshada Kupate
- Sachi Jagannath Mhatre
- Shravani Dhananjay Patil
- Sakshi Prakash Patil

---

## 📌 Project Status

✅ Final Year Engineering Project Completed Successfully

Deployment configuration improvements are currently in progress.

---

## 🌍 Domain

Artificial Intelligence | Computer Vision | Deep Learning | Environmental Monitoring

---

## 💙 Project Vision

The goal of Clean River AI is to demonstrate how Artificial Intelligence can be used to address real-world environmental challenges and contribute towards smarter and cleaner river ecosystems.

This project reflects the practical application of AI for environmental sustainability and highlights the potential of intelligent monitoring systems in solving real-world problems.
