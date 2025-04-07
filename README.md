# 🔮 Horoscope Predictor

Welcome to **Horoscope Predictor**, your cosmic bestie powered by machine learning and sprinkled with stardust. ✨  
Choose your zodiac sign and reveal a personalized horoscope — trained on real data, delivered with love (and an SVM model behind the scenes).

Built using Flask, HTML/CSS/JS, and a trained **SVM classifier**, this app bridges the mystical with the mathematical. ♡

---

## 🌟 Features

- 🔮 Predicts your horoscope based on your selected zodiac sign  
- 💻 Trained using real horoscope data (SVM, 93.97% accuracy baby!)  
- 🌈 Clean, dreamy UI with glowy animations  
- 🧠 Integrated ML model via Flask backend  
- 💫 Super smooth user experience (with a cute lil reveal button!)

---

## 💽 Tech Stack

| Frontend       | Backend        | Machine Learning                |
|----------------|----------------|---------------------------------|
| HTML, CSS, JS  | Python + Flask | SVM Classifier (scikit-learn)   |

---

## 🧠 How It Works

1. User picks a zodiac sign from the dropdown ♒️  
2. The sign is sent via POST request to Flask backend 🔁  
3. Flask returns a matching horoscope from a curated horoscope bank 🌙  
4. The app displays it with animation + ✨vibes✨  

> *Bonus*: The model was trained on a dataset of over **5,000 horoscope entries**, using SVM, Naive Bayes, and Random Forest.  
> **SVM** gave the best results and is the **only model used in the app**.

---

## 🚀 Run It Locally

Clone the repo and feel the universe unfold:

```bash
git clone https://github.com/yourusername/horoscope-predictor.git
cd horoscope-predictor
Install the necessary dependencies:

pip install -r requirements.txt
Then run the Flask app:

python app.py
Open your browser and go to http://127.0.0.1:5000 to reveal your fate ✨

🗂 Project Structure

horoscope-predictor/
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
├── templates/
│   └── index.html
├── models/
│   ├── SVM_horoscope.pkl         # ✅ used
│   ├── RF_horoscope.pkl          # ❌ not used
│   ├── NB_horoscope.pkl          # ❌ not used
│   └── vectorizer.pkl
├── app.py
├── requirements.txt
└── README.md

🧚‍♀️ Author
Made with love and a sprinkle of delusion by Swati Upadhyay 💫


