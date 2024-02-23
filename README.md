# Obsidian LLM Testing

## Why This Exists

- Specifically made for testing out local LLMs for Obsidian use.
- General knowledge should be a prerequisite for an LLM, so we're not testing that anymore. We're focusing on the quality of the answers when it comes to Obsidian / note-taking / personal knowledge management.

## How to Use

- The point of this is to test out your local LLM with questions that are relevant to your personal knowledge management system.

- Keep in mind, the questions found in `LLM_Test.md` are just examples. You should add your own questions, or modify the existing ones to better suit your needs. Just make sure to follow the same format and structure:

- A question is registered with each `**Q:**`.

- It will include all text in between one `**Q:**` and the next `**Q:**`.

```markdown
**Q:** [Question 1 here]
[anything in between these two Q's is part of question 1]
**Q:** [Question 2 here]
[anything between here and the next **Q:**, or if this is the last **Q:**, is registered as part of question 2]
```

### Prerequisites

- A decent computing system. I personally use 7B parameter models and I'm on an M1 Macbook Pro with 16GB of RAM.

### Start Up Your LLM Server

- I personally use LM Studio. Here's [a video showing how to get set up appropriately.](https://www.youtube.com/watch?v=SAKr008Z8NU)
- You can use any LLM server you want, but you'll need to modify the `main.py` file to point to your server.
- FYI, the default is `http://localhost:1234/v1`, found in the `openai_client.py` file.
- You can also use the OpenAI API directly, but you'll need to modify the `openai_client.py` file to use your API key... though IDK why you'd want to do that since the whole point of this is to test out local LLMs.

### Conducting Testing

- Once your server is up and running...
- Open up your terminal and navigate to the directory where you want to clone this repository.
- Run the following command to clone the repository:
  ```bash
  git clone https://github.com/systemsculpt/obsidian_llm_testing
  ```

````

- Navigate into the repository:
  ```bash
  cd obsidian_llm_testing
  ```
- Set up the virtual environment and install the requirements:
  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  ```
- Run the testing script:
  ```bash
  python main.py
  ```
- Follow the directions, and you're good to go!
- Results are placed in a `results` directory.

## Contribution

- Your contributions are welcome!
- If you have ideas for testing, automations, or improvements:
  - Fork this repository.
  - Make your changes and test them in Obsidian.
  - Submit a pull request with a description of your additions or changes.
````
