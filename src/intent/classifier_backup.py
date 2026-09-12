from src.intent.prompts import INTENTS


KEYWORDS = {
    "equipment_router": [
        "router",
        "ont",
        "equipment",
        "modem",
        "red light",
        "orange light",
        "router light",
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
        "account",
        "username",
        "my verizon",
    ],

    "installation_availability": [
        "installation",
        "install",
        "technician",
        "appointment",
        "availability",
        "service available",
        "setup",
        "order",
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


def classify_message(message: str) -> str:
    """
    Baseline #1:
    Simple keyword-based intent classifier.
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
        return "unknown"

    return best_intent
