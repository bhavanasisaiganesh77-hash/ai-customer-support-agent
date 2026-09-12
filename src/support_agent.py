from src.retrieval import SupportRetriever
from src.response_generator import ResponseGenerator
from src.intent.classifier import classify_message


class SupportAgent:

    def __init__(self):

        self.retriever = SupportRetriever()
        self.generator = ResponseGenerator()

    def respond(self, customer_message):

        intent = classify_message(customer_message)

        results = self.retriever.search(
            customer_message,
            top_k=5
        )

        if results.empty:
            retrieved_response = (
                "No matching support guidance was found."
            )
        else:
            retrieved_response = results.iloc[0]["support_response"]

        final_response = self.generator.generate_response(
            customer_message=customer_message,
            intent=intent,
            retrieved_response=retrieved_response
        )

        return {
            "customer_message": customer_message,
            "intent": intent,
            "retrieved_response": retrieved_response,
            "final_response": final_response
        }


if __name__ == "__main__":

    agent = SupportAgent()

    customer_message = input("Customer message: ")

    result = agent.respond(customer_message)

    print("\nDetected intent:")
    print(result["intent"])

    print("\nRetrieved support guidance:")
    print(result["retrieved_response"])

    print("\nFinal AI response:")
    print(result["final_response"])
