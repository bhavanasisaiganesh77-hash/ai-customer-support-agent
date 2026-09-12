import joblib

MODEL_PATH = "data/intent_classifier.joblib"

model = joblib.load(MODEL_PATH)

test_messages = [
    "My router has a red light",
    "My WiFi is not working",
    "The internet connection is very slow",
    "I cannot login to my Verizon account",
    "I forgot my account password",
    "How much is my monthly bill?",
    "Why was I charged an extra fee?",
    "I want to upgrade my phone plan",
    "What plans are available?",
    "I want to install Verizon internet",
    "Can a technician install the service?",
    "My Verizon mobile phone has no signal",
    "I cannot make calls from my phone",
    "My TV channel is not working",
    "I want to watch a movie on Fios TV",
    "I want to speak to a manager",
    "I want to file a complaint",
]

print("=" * 70)
print("ML CLASSIFIER TEST")
print("=" * 70)

for message in test_messages:
    prediction = model.predict([message])[0]
    
    print(f"\nMessage: {message}")
    print(f"Predicted intent: {prediction}")