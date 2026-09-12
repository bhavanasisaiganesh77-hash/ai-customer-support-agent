import os
from google import genai


class ResponseGenerator:

    def __init__(self):

        api_key = os.environ.get("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY environment variable is not configured."
            )

        self.client = genai.Client(api_key=api_key)
        self.model = "gemini-3.6-flash"


    def _fallback_response(self, customer_message, intent, retrieved_response):

        if not retrieved_response or retrieved_response.strip() == "":
            return (
                "I'm sorry, but I couldn't find a relevant support answer "
                "for your question. Please try asking your question in another way."
            )

        response = retrieved_response.strip()

        prefixes = {
            "billing_charges":
                "I understand your concern about your bill. ",
            "internet_wifi_issue":
                "I understand you're having trouble with your internet or Wi-Fi. ",
            "equipment_router":
                "I understand you're having an issue with your equipment. ",
            "tv_fios_content":
                "I understand you're having an issue with your TV service. ",
            "mobile_phone_issue":
                "I understand you're having an issue with your mobile service. ",
            "account_login":
                "I understand you're having trouble accessing your account. ",
            "installation_availability":
                "I understand you're asking about installation or service availability. ",
            "plan_product_upgrade":
                "I understand you're asking about your plan or service options. ",
            "complaint_escalation":
                "I understand your concern and want to help address it. "
        }

        prefix = prefixes.get(
            intent,
            "I understand your concern. "
        )

        if response.lower().startswith(prefix.lower()):
            return response

        return prefix + response


    def generate_response(
        self,
        customer_message,
        intent,
        retrieved_response
    ):

        prompt = f"""
You are a professional Verizon customer-support assistant.

Customer message:
{customer_message}

Detected intent:
{intent}

Retrieved support guidance:
{retrieved_response}

Write the best possible customer-facing support response.

Strict rules:
- Be polite, concise, clear, and helpful.
- Directly address the customer's issue.
- Use ONLY the retrieved support guidance as factual support information.
- Do not invent facts, policies, prices, phone numbers, links, URLs, promotions, or procedures.
- Do not create fake links or phone numbers.
- Do not claim an action was completed unless explicitly supported.
- Do not promise refunds, discounts, upgrades, appointments, or replacements unless explicitly supported.
- Do not mention AI, Gemini, retrieval, classification, datasets, or internal systems.
- Return ONLY the customer-facing response.
""".strip()

        try:

            response = self.client.models.generate_content(
                model=self.model,
                contents=prompt
            )

            return response.text.strip()

        except Exception as e:

            error_text = str(e)

            if "429" in error_text or "RESOURCE_EXHAUSTED" in error_text:
                return self._fallback_response(
                    customer_message,
                    intent,
                    retrieved_response
                )

            if "503" in error_text or "UNAVAILABLE" in error_text:
                return self._fallback_response(
                    customer_message,
                    intent,
                    retrieved_response
                )

            return self._fallback_response(
                customer_message,
                intent,
                retrieved_response
            )
