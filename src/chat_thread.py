from PySide6.QtCore import QThread, Signal

class ChatThread(QThread):
    new_message_signal = Signal(str)

    def __init__(self, client, history, temperature):
        super().__init__()
        self.client = client
        self.history = history
        self.temperature = temperature

    def run(self):
        completion = self.client.chat.completions.create(
            model="local-model",
            messages=self.history,
            temperature=self.temperature,
            stream=True,
        )

        new_message = {"role": "assistant", "content": ""}
        for chunk in completion:
            if chunk.choices[0].delta.content:
                new_message_content = chunk.choices[0].delta.content
                self.new_message_signal.emit(new_message_content)
                new_message["content"] += new_message_content

        self.history.append(new_message)