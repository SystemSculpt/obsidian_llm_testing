from openai import OpenAI

def initialize_client():
    return OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def get_completion(client, history, temperature=0.7, stream=True):
    return client.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=history,
        temperature=temperature,
        stream=stream,
    )