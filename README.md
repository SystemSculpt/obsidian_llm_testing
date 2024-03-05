# Obsidian LLM Testing GUI

## Overview

- This project provides a graphical user interface (GUI) application for testing local Large Language Models (LLMs) within the context of Obsidian or similar note-taking and personal knowledge management systems.

- It aims to facilitate the evaluation of LLMs' performance on tasks relevant to knowledge management, note-taking, and productivity.

## Features

- **Local LLM Integration**: Connect to local LLM servers for privacy-focused, offline testing.
- **Customizable Tests**: Easily modify or add new test questions to suit your specific needs.
- **Interactive GUI**: Conduct tests and review results through a user-friendly interface.
- **Performance Metrics**: Track and analyze the performance of your LLM with built-in scoring and feedback mechanisms.

## To Do

- [ ] Add a screenshot of the GUI to the README.
- [ ] Add a GIF of the GUI in action to the README.
- [ ] Add a section on how to contribute to the project.
- [ ] Add a section on how to add new test questions.

## Getting Started

### Prerequisites

- Python 3.6 or higher.
- A local LLM server or access to an LLM API (e.g., OpenAI's GPT models).
- An environment capable of running PyQt6 applications.

### Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/systemsculpt/obsidian_llm_testing
cd obsidian_llm_testing
```

2. **Set Up a Virtual Environment** (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

### Configuration

1. **Edit the Configuration File**: Modify `config.yaml` to set up your LLM server URL, API key (if needed), and other preferences like font size and window size.

2. **Prepare Your Test Questions**: Edit `LLM_Test.md` to include your custom questions. Follow the format provided in the file for consistency.

### Running the Application

- Launch the GUI application by running:

```bash
python main.py
```

- The GUI will start, and you can begin testing by following the on-screen instructions.

## Usage

- **Connect to Your LLM Server**: Use the "Reload API Connection" button to connect to your LLM server.
- **Generate Answers**: Select a question and use the "Generate Answer" button to get responses from your LLM.
- **Evaluate Responses**: Mark answers as "Pass" or "Fail" based on their relevance and accuracy.
- **Review Results**: The application automatically calculates and displays performance metrics.

## Customization

- **Adding New Questions**: You can add new questions directly to the `LLM_Test.md` file. Ensure you follow the existing format for compatibility.
- **Changing the GUI Appearance**: Modify settings in `config.yaml` to adjust the font size, window size, and other UI elements.

## Contribution

Contributions to improve the application or add new features are welcome. Please follow these steps:

1. **Fork the Repository**: Create your own fork of the project.
2. **Make Your Changes**: Implement your improvements or new features.
3. **Test Your Changes**: Ensure your changes work as expected, especially with Obsidian.
4. **Submit a Pull Request**: Create a PR against the main project with a clear description of your changes.

Thank you for contributing to the Obsidian LLM Testing GUI project!
