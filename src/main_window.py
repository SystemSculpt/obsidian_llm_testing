from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QTextEdit, QHBoxLayout, QListWidget, QListWidgetItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QTextCursor
from .utils import load_config, initialize_client, get_model_name, load_questions_from_file
from .chat_thread import ChatThread


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = load_config("config.yaml")

        self.setWindowTitle("LLM Testing with PySide6")
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(1400, 800)

        self.client = initialize_client(self.config["base_url"], self.config["api_key"])
        self.model_name = get_model_name(self.client)
        self.questions = load_questions_from_file(self.config["questions_file"])

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        self.question_list = QListWidget()
        self.question_list.currentItemChanged.connect(self.display_question_from_list)
        main_layout.addWidget(self.question_list, 1)
        self.question_list.setWordWrap(True)
        self.question_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        for question in self.questions:
            question_preview = question[:50] + "..." if len(question) > 50 else question
            item = QListWidgetItem(question_preview)
            item.setData(Qt.UserRole, question)
            self.question_list.addItem(item)

        self.qa_layout = QVBoxLayout()
        self.model_label = QLabel(f"Model: {self.model_name}" if self.model_name else "No Model Loaded")
        self.qa_layout.addWidget(self.model_label)

        self.question_display = QTextEdit()
        self.question_display.setReadOnly(True)
        self.qa_layout.addWidget(self.question_display)

        self.answer_display = QTextEdit()
        self.answer_display.setReadOnly(True)
        self.qa_layout.addWidget(self.answer_display)

        self.generate_answer_btn = QPushButton("Generate Answer")
        self.generate_answer_btn.clicked.connect(self.generate_answer)
        self.qa_layout.addWidget(self.generate_answer_btn)


        main_layout.addLayout(self.qa_layout, 3)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def display_question_from_list(self, current, _):
        self.stop_answer_generation()  # Add this line to stop answer generation
        if current:
            full_question = current.data(Qt.UserRole)
            self.display_question(full_question)
            self.answer_display.clear()

    def display_question(self, question):
        self.question_display.setText(question)
        self.answer_display.clear()

    def generate_answer(self):
        self.stop_answer_generation()  # Add this line to stop previous generation
        question = self.question_display.toPlainText()
        if question:
            self.answer_display.clear()
            system_prompt = self.config["system_prompt"]
            temperature = self.config["temperature"]
            history = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ]
            self.chat_thread = ChatThread(self.client, history, temperature)
            self.chat_thread.new_message_signal.connect(self.update_answer_display)
            self.chat_thread.start()

    def update_answer_display(self, message):
        self.answer_display.moveCursor(QTextCursor.End)
        self.answer_display.insertPlainText(message)
    def stop_answer_generation(self):
        if hasattr(self, 'chat_thread') and self.chat_thread.isRunning():
            self.chat_thread.terminate()
            self.chat_thread.wait()
            del self.chat_thread
    def remove_widget_from_layout(self, widget):
        widget.hide()
        self.qa_layout.removeWidget(widget)
