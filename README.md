# Obsidian LLM Testing

- Specifically made for testing out local LLMs for Obsidian use.
- Designed to enhance your productivity and creativity.

## Repository Contents

- `LLM Test Answer Sheet` is the answer sheet, providing GPT-4 level quality answers (since it's... well, the best).
- `LLM Test` is the blank testing sheet with questions only and blank A: spots where you should put the specific LLM's answers into.

## How to Use

### Prerequisites
- A decent computing system. We're using 7B parameter models here for now, and I'm on an M1 Macbook Pro with 16GB of RAM.
- The more RAM/better processor you have, the (much) better.
- Obsidian's Text Generator plugin knowledge. [Here's a good video to start with and get a local LLM running.](https://www.youtube.com/watch?v=c2Ug6U6O5Cg)
- Here's [another video showing how to get set up appropriately, so check this one out too.](https://www.youtube.com/watch?v=SAKr008Z8NU)

### Conducting Testing
#### Manually
1. Make sure you've set everything up and loaded the local LLM (see videos above if you don't understand).
2. Create a copy of the LLM Test sheet and name it appropriately so you have a reference as to which model you're testing.
3. Copy a question into a brand new note.
4. Use the "Generate Text!" command from Text Generator, either via command palette or your designated hotkey.
5. Copy the generated answer once your LLM is finished processing into the test sheet.
6. Rinse and repeat for all the questions.
7. Reference the completed test sheet vs. the `LLM Test Answer Sheet` and see how many it got correct.
8. Suggestion: name the test sheet as the model name and then the total score at the end (ex. `Zephyr 7B 8-20`)
#### "Automatic"
1. Install [Python](https://www.python.org/) if not already installed
2. Install the [OpenAI Python API](https://pypi.org/project/openai/) by running `pip install openai` in a terminal / commandline if not already installed
3. Make sure you've loaded a local LLM (see above video for refference)
4. Start the automatic Testing script by either
  - starting the file `llm_test.py` by doubleclicking it or
  - executing `python llm_tester.py` (`py llm_tester.py` on Windows) in a terminal
6. Provide the script the required infomations, once it outputs "generating answer for:" it asks all Questions from the `LLM Test` file and exists once that's complete
7. Reference the completed test sheet vs. the `LLM Test Answer Sheet` and see how many it got correct.
8. Suggestion: name the test sheet as the model name and then the total score at the end (ex. `Zephyr 7B 8-20`)

## Contribution

- Your contributions are welcome!
- If you have ideas for testing, automations, or improvements:
  - Fork this repository.
  - Make your changes and test them in Obsidian.
  - Submit a pull request with a description of your additions or changes.

## Support

- Your support helps me, Mike, dedicate more time to creating and refining.

<p>
  <a href="https://www.patreon.com/SystemSculpt">
    <img
      align="left"
      src="https://indigenousx.com.au/wp-content/uploads/2017/03/patreon-medium-button.png"
      height="50"
      width="210"
      alt="Support on Patreon"
  /></a>
  <a href="https://www.buymeacoffee.com/SystemSculpt">
    <img
      align="left"
      src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
      height="50"
      width="210"
      alt="Buy Me A Coffee"
  /></a>
</p>
