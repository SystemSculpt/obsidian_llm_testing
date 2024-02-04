from openai import OpenAI, APIConnectionError
import time

def initialize_client():
    return OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def get_completion(client, history, temperature=0.7, stream=True):
    while True:
        try:
            return client.chat.completions.create(
                model="local-model",  # this field is currently unused
                messages=history,
                temperature=temperature,
                stream=stream,
            )
        except APIConnectionError:
            print("\nConnection error. Ensure your LLM is running and accessible at http://localhost:1234/v1")
            print("Check if the LLM service is running and listening on the correct port.")
            print("Press Enter to try connecting again, or Ctrl+C to exit.")
            input()
