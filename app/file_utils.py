import os
import re
from datetime import datetime

def create_results_directory(llm_name):
    results_dir = f"./results/{llm_name}"
    os.makedirs(results_dir, exist_ok=True)
    return results_dir

def extract_version(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        version_match = re.search(r'Version: (\d+\.\d+)', content)
        if version_match:
            return version_match.group(1)
        else:
            raise ValueError("Version not found in the file.")

def get_current_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M")

def extract_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(r'- \*\*Q:\*\* (.*?)(?=\n\n- \*\*A:\*\*|$)', content, re.DOTALL)
        questions.extend(matches)
    return questions

def write_to_file(file_path, content):
    with open(file_path, 'a') as file:
        file.write(content)