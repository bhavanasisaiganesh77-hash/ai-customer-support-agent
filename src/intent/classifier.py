import joblib

MODEL_PATH = "data/intent_classifier.joblib"

# Load trained ML model
ml_model = joblib.load(MODEL_PATH)

KEYWORDS = {
    "equipment_router": [
        "router",
        "ont",
        "modem",
        "equipment",
        "red light",
        "orange light",
        "router light",
        "red indicator",
        "orange indicator",
        "device in my house",
    ],

    "internet_wifi_issue": [
        "internet",
        "wifi",
        "wi-fi",
        "no connection",
        "slow internet",
        "slow speed",
        "connection",
        "network",
        "offline",
        "can't get online",
        "cannot get online",
        "get online",
        "online at home",
    ],

    "tv_fios_content": [
        "tv",
        "television",
        "channel",
        "dvr",
        "streaming",
        "movie",
        "show",
        "fios tv",
    ],

    "billing_charges": [
        "bill",
        "billing",
        "charge",
        "charged",
        "payment",
        "fee",
        "price",
        "refund",
    ],

    "account_login": [
        "login",
        "log in",
        "sign in",
        "password",
        "username",
        "my verizon",
        "account",
    ],

    "installation_availability": [
        "installation",
        "install",
        "technician",
        "appointment",
        "availability",
        "service available",
        "setup",
    ],

    "mobile_phone_issue": [
        "mobile",
        "phone",
        "cell",
        "lte",
        "5g",
        "calling",
        "call",
        "wireless coverage",
        "no signal",
    ],

    "plan_product_upgrade": [
        "plan",
        "upgrade",
        "promotion",
        "promo",
        "switch",
        "product",
        "package",
    ],

    "complaint_escalation": [
        "complaint",
        "manager",
        "supervisor",
        "human",
        "agent",
        "escalate",
        "escalation",
    ],
}


def keyword_classify(message: str):
    """
    Classify using domain-specific keywords.
    Returns None when no useful keyword is found.
    """
    message = message.lower()

    scores = {}

    for intent, keywords in KEYWORDS.items():
        score = 0

        for keyword in keywords:
            if keyword in message:
                score += 1

        scores[intent] = score

    best_intent = max(scores, key=scores.get)

    if scores[best_intent] == 0:
        return None

    return best_intent


def classify_message(message: str) -> str:
    """
    Hybrid intent classifier.

    1. Try domain-specific keyword matching.
    2. If no keyword matches, use the trained ML model.
    """
    keyword_result = keyword_classify(message)

    if keyword_result is not None:
        return keyword_result

    prediction = ml_model.predict([message])[0]

    return prediction
