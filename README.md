# 🩺 Blood Pressure Stage Predictor Web Application

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web_Framework-000000.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

A machine learning-powered web application developed using **Flask** that predicts **blood pressure risk stages** based on basic user input. It combines a trained ML model with a clean, responsive frontend to serve as a browser-based health advisory tool.

---

## 🔍 Overview

This project demonstrates the integration of a supervised machine learning model with a web application interface. Users can input relevant health data and receive a prediction of their blood pressure classification.

**Project Goals:**

- Implement a supervised ML model using `scikit-learn`.
- Build an interactive and clean frontend using HTML, CSS, and JavaScript.
- Use Flask to bridge backend ML logic with frontend views.
- Provide clear, actionable health feedback to the user.

---

## 🌐UI look:

---
## Landing-Page(Home)
<img src="/static/WebsiteLook/Landing-HomePage.png">









## 🗂️ Project Structure

```
📁 project/
├── app.py               → Flask backend
├── model.pkl            → Trained ML model (excluded via .gitignore)
├── encoders.pkl         → Encoders for categorical input(excluded via .gitignore)
├── requirements.txt     → Project dependencies
├── templates/
│   ├── index.html       → Home page
│   ├── predict.html     → User input form
│   ├── result.html      → Prediction display
│   └── details.html     → Informational page
├── static/
│   ├── style.css        → Custom styling
│   └── script.js        → Frontend interactivity
├── flaskenv/            → Local Flask environment config (ignored)
└── dataset/             → Training dataset (ignored)
```

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/bp-predictor.git
cd bp-predictor
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to start using the app.


## 🛠️ Tech Stack

- **Programming Language:** Python 3
- **Web Framework:** Flask
- **Machine Learning:** scikit-learn, pandas
- **Frontend:** HTML, CSS, JavaScript
- **Templating Engine:** Jinja2
- **Model Serialization:** Pickle

---

## 📁 .gitignore Highlights

Files and directories excluded from version control:

```
*.pkl
flaskenv/
__pycache__/
.env
```

---

## 👩‍💻 About the Developer

**Srashti Shukla**  
B.Tech Computer Science undergraduate, passionate about full-stack web development and applied machine learning. Enthusiastic about building real-world tech solutions.

📫 Email: [srashtishukla1111@gmail.com](mailto:srashtishukla1111@gmail.com)  

---

## ⭐ Support

If you found this project useful, please consider starring the repository.  
Your support helps improve and maintain this work. Thank you!
