# Student_Lifestyle_and_Stress_Prediction_project_SVM
# 🧠 Student Lifestyle and Stress Prediction

A Machine Learning web application that predicts whether a student is experiencing stress based on lifestyle and academic factors using a Support Vector Machine (SVM) model.

## 🚀 Live Demo

🔗 https://student-lifestyle-and-stress-prediction-3t3v.onrender.com/

---

## 📌 Project Overview

Student stress is influenced by various lifestyle and academic factors. This project uses Machine Learning to analyze these factors and predict whether a student is likely to be stressed.

The application is built with Streamlit and deployed on Render, providing real-time predictions through an interactive web interface.

---

## 🎯 Features

- Real-Time Stress Prediction
- Attractive Streamlit User Interface
- Machine Learning Powered Predictions
- Easy-to-Use Dashboard
- Responsive Design
- Render Deployment

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- NumPy
- Pandas
- Pickle
- Render

---

## 🤖 Machine Learning Algorithm

### Support Vector Machine (SVM)

Support Vector Machine (SVM) is a supervised machine learning algorithm used for classification tasks. It identifies the optimal decision boundary that separates different classes effectively.

In this project, SVM is used to classify students into:

- 😊 Not Stressed
- ⚠️ Stressed

---

## 📂 Project Structure

```text
Student-Stress-Prediction/
│
├── app.py
├── svm.pkl
├── requirements.txt
├── README.md
│
└── assets/
```

---

## 📊 Input Features

The model uses the following inputs:

| Feature | Description |
|----------|-------------|
| Student Type | Day Scholar / Hosteller |
| Sleep Hours | Average sleep per day |
| Study Hours | Daily study duration |
| Social Media Hours | Daily social media usage |
| Attendance | Attendance percentage |
| Exam Pressure | Academic pressure level |
| Family Support | Family support rating |
| Month | Month number |

---

## 📈 Prediction Output

The model predicts:

### 😊 Not Stressed

or

### ⚠️ Stressed

based on the student's lifestyle and academic habits.

---

## ⚙️ Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/student-stress-prediction.git
```

### Step 2: Move into Project Folder

```bash
cd student-stress-prediction
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run Application

```bash
streamlit run app.py
```

---

## 🌐 Render Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 📷 Application Workflow

1. Enter student lifestyle details.
2. Click on Predict Stress Level.
3. Model analyzes the inputs.
4. Prediction is displayed instantly.
5. User receives stress classification.

---

## 📊 Dataset

Dataset Used:

Student Lifestyle and Stress Prediction Dataset

The dataset contains lifestyle, academic, and behavioral factors that influence student stress levels.

---

## 🔮 Future Enhancements

- Stress Probability Score
- Data Visualization Dashboard
- Student Performance Analysis
- Multiple ML Model Comparison
- Personalized Stress Management Suggestions
- User Authentication System

---

## 👨‍💻 Author

### Omkar Raut

Aspiring Data Analyst | Python Developer | Machine Learning Enthusiast

---

## 🌐 Live Application

🔗 https://student-lifestyle-and-stress-prediction-3t3v.onrender.com/

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Your support motivates further development and improvements.

---


---

### Made with ❤️ using Python, Streamlit, and Machine Learning
