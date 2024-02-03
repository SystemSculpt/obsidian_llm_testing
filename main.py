from app.test_handler import initialize_test, handle_questions, finalize_grading
from app.file_utils import write_to_file

def main():
    llm_name, results_dir, version, current_datetime, test_file_path, questions, client = initialize_test()
    write_to_file(test_file_path, f"# Test v{version} {current_datetime}\n\n## {llm_name}\n\n")
    pass_count, total_count = handle_questions(test_file_path, questions, client)
    finalize_grading(test_file_path, pass_count, total_count)

if __name__ == "__main__":
    main()