from openai import OpenAI, APIConnectionError
import time

# Global variable to store the model name
model_name = None

def initialize_client():
    global model_name
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    model_name = check_and_get_model_name(client)
    return client

def check_and_get_model_name(client):
    while True:
        try:
            model_name = get_model_name(client)
            print(f"\nTesting model: {model_name}")
            if not model_name:  # Check if model_name is empty or None
                raise APIConnectionError("No active model found. Ensure your LLM is running and accessible.")
            return model_name
        except APIConnectionError as e:
            handle_connection_error(e)
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            exit(0)

def get_model_name(client):
    try:
        response = client.models.list().data[0]
        model_id = response.id
        model_name = extract_model_name_from_id(model_id)
        return model_name
    except IndexError:  # Handle the case where the response data is empty
        return None

def extract_model_name_from_id(model_id):
    # Extract the model name from the id attribute
    model_name = model_id.split('/')[-1]
    return model_name

def get_completion(client, history, temperature=0.2, stream=True):
    while True:
        try:
            return client.chat.completions.create(
                model=model_name,  # Use the global variable
                messages=history,
                temperature=temperature,
                stream=stream,
            )
        except APIConnectionError as e:
            handle_connection_error(e)
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            exit(0)

def handle_connection_error(e):
    print(f"\n{e}")
    print("Ensure your LLM is running and accessible at http://localhost:1234/v1")
    print("Check if the LLM service is running and listening on the correct port.")
    try:
        print("Press Enter to try connecting again, or Ctrl+C to exit.")
        input()
    except KeyboardInterrupt:
        print("\n\nExiting application...")
        exit(0)
