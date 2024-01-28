from openai import OpenAI
from pathlib import Path

messageHistory = [{"role": "system", "content": "Answer in short, presize sentenses."}]


def getAnswer(api: OpenAI, message: str) -> str:
    """
    Sends a message to the OpenAI API and retrieves the corresponding answer.

    This function formats the input message, sends it to the OpenAI API, and
    retrieves the response. Both the message and the response are appended to
    the global `messageHistory`. The function ensures that both input and output
    messages are stripped of leading and trailing whitespace.

    Args:
        api (openai.OpenAI): An instance of the OpenAI API client.
        message (str): The message string to send to the OpenAI API.

    Returns:
        str: The content of the answer received from the OpenAI API, stripped of
        leading and trailing whitespace.

    Global Variables:
        messageHistory (List[Dict[str, str]]): A list of message dictionaries maintaining
        the history of interactions. Each dictionary has 'role' and 'content' as keys.
    """
    global messageHistory

    # Ensure the message has no leading/trailing whitespace.
    message = message.strip()

    messageHistory.append({"role": "user", "content": message})

    # Send the message to the API and get the response.
    completion = api.chat.completions.create(
        model="local-model",  # this field is currently unused
        messages=messageHistory
    )

    # add the answer to the history and return it
    answer = completion.choices[0].message
    messageHistory.append(answer)
    return answer.content.strip()


def main() -> None:
    api = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
    with Path("LLM Test.md").open('r', encoding='UTF-8') as inputFile:
        outputFilePath = input("what should the name of the result file be? ").strip()
        with Path(outputFilePath).open('w', encoding='UTF-8') as outputFile:
            for line in inputFile:
                if line.startswith('- Q: '):
                    outputFile.write(line)
                    print("generating answer for:", line[5:].strip())
                    outputFile.write('- A: ' + getAnswer(api, line[5:]) + '\n')
                elif line.startswith('- A:'):
                    pass
                else:
                    outputFile.write(line)


if __name__ == '__main__':
    main()
