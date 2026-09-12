INTENTS = {
    "equipment_router": "Router, ONT, equipment setup, status lights, troubleshooting, or equipment return.",
    
    "internet_wifi_issue": "Internet or Wi-Fi outage, slow speed, connectivity, or network performance issues.",
    
    "tv_fios_content": "TV channels, DVR, streaming, movies, shows, or TV programming issues.",
    
    "billing_charges": "Bills, unexpected charges, fees, payments, or subscription billing issues.",
    
    "account_login": "My Verizon login, account access, or account-related access problems.",
    
    "installation_availability": "Installation, technician appointments, service availability, ordering, or setup.",
    
    "mobile_phone_issue": "Mobile phone, LTE, wireless coverage, calling, or mobile device problems.",
    
    "plan_product_upgrade": "Plans, promotions, product choices, switching, or upgrading services.",
    
    "complaint_escalation": "Customer-service complaints, manager requests, or human/regulatory escalation."
}


def build_classification_prompt(message: str) -> str:
    intent_list = "\n".join(
        f"- {name}: {description}"
        for name, description in INTENTS.items()
    )

    return f"""
You are a customer-support intent classifier for VerizonSupport.

Classify the customer message into exactly ONE of the following intents:

{intent_list}

Customer message:
"{message}"

Return ONLY the intent name.
Do not provide an explanation.
"""