import re
import yaml
from openai import OpenAI, APIConnectionError

def load_config(config_path="config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)

def initialize_client(base_url, api_key):
    try:
        return OpenAI(base_url=base_url, api_key=api_key)
    except APIConnectionError:
        return None

def get_model_name(client):
    if client is None:
        return None
    try:
        response = client.models.list().data[0]
        model_id = response.id
        return model_id.split("/")[-1]
    except IndexError:
        return None

def load_questions_from_file(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.read()
            pattern = r"\*\*Q:\*\*((?:.|\n)*?)(?=\n\*\*Q:\*\*|\Z)"
            questions = re.findall(pattern, content, re.DOTALL)
        return questions
    except FileNotFoundError:
        return []