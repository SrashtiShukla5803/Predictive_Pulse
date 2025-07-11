# 💉 Blood Pressure Stage Predictor Web App 🧠💻

Hey there! 👋  
This is a **Flask + Machine Learning** web app that predicts **blood pressure risk** levels based on some basic inputs.  
Yup, your browser becomes a little health advisor now. 💡

---

## ✨ What’s This App About?

This project was built to:
- 🧪 Try out a simple ML model (trained using Python + scikit-learn)
- 🎨 Build a clean frontend using HTML/CSS/JS (styled by yours truly)
- 🔥 Connect the brains (ML) to the beauty (frontend) using Flask

So now, you enter some info → it thinks a bit 🤔 → and tells you what BP risk you’re in!

---

## 🗂️ Folder Vibes

Here’s how the project’s organized (neatly, ofc):

```
📁 project/
├── app.py               → Flask backend
├── model.pkl            → Trained ML model (you won’t see it on GitHub, it’s ignored)
├── encoders.pkl         → For input pre-processing
├── requirements.txt     → All the pip packages
├── templates/           → All HTML pages (Jinja-powered)
│   ├── index.html       → Welcome!
│   ├── predict.html     → Form for inputs
│   ├── result.html      → Shows prediction
│   └── details.html     → Extra info
├── static/
│   ├── style.css        → Custom styling
│   └── script.js        → JS magic
├── flaskenv/            → My local settings (ignored)
└── dataset/             → The training data (also ignored)
```

---


### 💾 Clone It!
```bash
git clone https://github.com/your-username/bp-predictor.git
cd bp-predictor
```

### 🐍 Virtual Environment (be a good dev)
```bash
python -m venv venv
source venv/bin/activate    # For Windows: venv\Scripts\activate
```

### 📦 Install the Stuff
```bash
pip install -r requirements.txt
```

### 🚀 Fire It Up
```bash
python app.py
```

Now head to `http://127.0.0.1:5000` in your browser and you're live! 🔥

---

## 🤖 Tech Stack (a.k.a the cool tools)

- **Python 3**
- **Flask**
- **scikit-learn**
- **pandas**
- **HTML / CSS / JS**
- **Jinja2 templates**
- **Pickle** (to save my model and encoder like a snack)

---

## 🧽 What I Don’t Push (thanks `.gitignore`)

```gitignore
# Don't peek 👀
*.pkl
flaskenv/
dataset/
__pycache__/
.env
```

---

## 🧑‍🎓 About Me

Hi, I'm **Srashti Shukla** —  
a student dev who builds cool stuff between coffee breaks and crash courses ☕👩‍💻

📫 [Email Me](srashtishukla1111@gmail.com)
🌐 [My website](link)
🐍 Python is life

---

## ⭐ If You Like It...

Give this repo a ⭐  
It costs $0 but makes my day 😄
