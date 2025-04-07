from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load("models/SVM_horoscope.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# Label to sign mapping
label_to_sign = {
    0: "Aries", 1: "Taurus", 2: "Gemini", 3: "Cancer",
    4: "Leo", 5: "Virgo", 6: "Libra", 7: "Scorpio",
    8: "Sagittarius", 9: "Capricorn", 10: "Aquarius", 11: "Pisces"
}

# Horoscope message bank
horoscope_bank = {
    "Aries": "🔥 Today you lead like a warrior. Let no one dim that spark.",
    "Taurus": "🌸 Comfort is queen, but adventure whispers your name.",
    "Gemini": "💬 Your words can start revolutions. Choose them wisely.",
    "Cancer": "🌊 Feel deeply, love freely. Your heart is your compass.",
    "Leo": "🦁 Shine, roar, repeat. You are the spotlight.",
    "Virgo": "📚 Perfection isn't the goal—authenticity is.",
    "Libra": "⚖️ Harmony is your superpower. Spread that peace.",
    "Scorpio": "🦂 Secrets swirl, truths rise. Trust your instincts.",
    "Sagittarius": "🏹 Adventure calls, and babe, you're the answer.",
    "Capricorn": "🧗 Grind now, glow later. Your empire awaits.",
    "Aquarius": "🛸 Rebel with a cause. The future needs your ideas.",
    "Pisces": "🎨 Your dreams paint reality. Don’t stop imagining."
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    selected_sign = data.get("sign")

    if not selected_sign:
        return jsonify({"error": "No zodiac sign provided"}), 400

    # Find index of sign to simulate model prediction (you can skip model if not needed)
    sign_index = list(label_to_sign.values()).index(selected_sign.capitalize())

    # DEBUG PRINTS
    print("Received sign:", selected_sign)
    print("Predicted label:", sign_index)

    # Get horoscope from the bank
    horoscope_message = horoscope_bank.get(selected_sign.capitalize(), "✨ The stars are silent today, but your story isn't over ✨")

    return jsonify({
        "prediction": selected_sign.capitalize(),
        "horoscope": horoscope_message
    })

if __name__ == "__main__":
    app.run(debug=True)
