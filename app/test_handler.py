import os
import re
from app.file_utils import write_to_file, create_results_directory, extract_version, get_current_datetime, extract_questions_from_file
from app.openai_client import initialize_client, get_completion, get_model_name
from app.config import SEPARATOR, GREEN, CYAN, YELLOW, RESET

def initialize_test(llm_name=None):
    client = initialize_client()
    llm_name = get_model_name(client)
    version = extract_version('LLM Test.md')
    results_dir = create_results_directory(llm_name, version)
    current_datetime = get_current_datetime()
    test_file_path = os.path.join(results_dir, f"{current_datetime}.md")
    questions = extract_questions_from_file('LLM Test.md')
    return llm_name, results_dir, version, current_datetime, test_file_path, questions, client

def process_question(question, client, test_file_path):
    print(SEPARATOR)
    history = [
        {"role": "system", "content": "You are an intelligent assistant. You always provide well-reasoned answers that are both correct and helpful."},
        {"role": "user", "content": question.strip()},
    ]
    completion = get_completion(client, history)
    buffer = ""
    write_to_file(test_file_path, f"## Q:\n{question.strip()}\n\n## A:\n")
    print(f"{CYAN}Q:{RESET}\n{CYAN}{question.strip()}{RESET}\n")
    print(f"{YELLOW}A:{RESET}")
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:
            print(f"{YELLOW}{content}{RESET}", end="", flush=True)
            buffer += content
            if "\n" in content:
                lines = buffer.split("\n")
                for line in lines[:-1]:
                    write_to_file(test_file_path, line + "\n")
                buffer = lines[-1]
    write_to_file(test_file_path, buffer + "\n\n")

def grade_response():
    try:
        grade = input("\n\nThat's the end of the LLM's response.\nDid the LLM pass according to your personal response preferences? (y/n) ")
        while grade not in ['y', 'n']:
            grade = input("\nOnly type y for Yes or n for No; Did the LLM pass according to your personal response preferences? (y/n) ")
        return grade == 'y'
    except KeyboardInterrupt:
        print("\n\nExiting application...")
        exit(0)

def handle_questions(test_file_path, questions, client):
    pass_count = 0
    total_count = 0
    for question in questions:
        try:
            process_question(question, client, test_file_path)
        except KeyboardInterrupt:
            print("\n\nLLM's response was interrupted. Ending answer here.")
            write_to_file(test_file_path, "\n\n## Answer Interrupted\n\n")
        finally:
            if grade_response():
                write_to_file(test_file_path, "## Grade: PASS!\n\n")
                pass_count += 1
            else:
                write_to_file(test_file_path, "## Grade: FAIL.\n\n")
            total_count += 1
    return pass_count, total_count

def finalize_grading(test_file_path, pass_count, total_count):
    final_grade = f"\n\n## Final Grade: {pass_count}/{total_count}\n"
    with open(test_file_path, 'r') as file:
        content = file.read()
    position = re.search(r"\n(## .+)", content).end()
    updated_content = content[:position] + final_grade + content[position:]
    with open(test_file_path, 'w') as file:
        file.write(updated_content)

def run_tests_loop():
    llm_name = None
    while True:
        llm_name, results_dir, version, current_datetime, test_file_path, questions, client = initialize_test(llm_name)
        write_to_file(test_file_path, f"# Test v{version} {current_datetime}\n\n## {llm_name}\n\n")
        pass_count, total_count = handle_questions(test_file_path, questions, client)
        finalize_grading(test_file_path, pass_count, total_count)
        
        print(f"\nTesting Complete. Final Score: {pass_count}/{total_count}")
        
        retry = input("Do you want to run the test again? (y/n): ").strip().lower()
        if retry != 'y':
            print("Exiting the testing process. Goodbye!")
            break