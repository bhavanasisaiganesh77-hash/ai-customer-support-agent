from classifier import classify_message


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


for message in test_messages:
    intent = classify_message(message)

    print(f"\nMessage: {message}")
    print(f"Predicted intent: {intent}")