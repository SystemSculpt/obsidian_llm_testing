from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QTextCursor, QFont, QColor, QBrush
from .utils import (
    load_config,
    initialize_client,
    get_model_name,
    load_questions_from_file,
)
from .chat_thread import ChatThread
from .ui import initUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.config = load_config("config.yaml")

        self.setWindowTitle("LLM Testing with PySide6")
        window_size = self.config.get("window_size", [800, 600])
        self.setGeometry(100, 100, *window_size)
        self.setFixedSize(*window_size)

        try:
            self.client = initialize_client(
                self.config["base_url"], self.config["api_key"]
            )
            self.model_name = get_model_name(self.client)
        except Exception as e:
            print(f"Error initializing API connection: {e}")
            self.model_name = "Model Offline / Connectivity Error"

        self.questions = load_questions_from_file(self.config["questions_file"])

        # Set global font size for the application
        font_size = self.config.get("font_size", 12)  # Default to 12 if not specified
        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)

        self.initUI()
        self.graded_questions = set()

    def initUI(self):
        initUI(self)

    def display_question_from_list(self, current, _):
        self.stop_answer_generation()
        if current:
            full_question = current.data(Qt.UserRole)
            self.display_question(full_question)
            self.answer_display.clear()

    def display_question(self, question):
        self.question_display.setText(question)
        self.answer_display.clear()

    def generate_answer(self):
        self.stop_answer_generation()
        question = self.question_display.toPlainText()
        if question:
            self.generate_answer_btn.setText("Generating")
            self.dot_count = 1
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.update_button_text)
            self.timer.start(500)  # Update every 500 milliseconds
            # Disable UI components
            self.question_list.setEnabled(False)
            self.pass_btn.setEnabled(False)
            self.fail_btn.setEnabled(False)
            self.generate_answer_btn.setEnabled(False)
            self.reload_api_btn.setEnabled(False)
            self.custom_question_btn.setEnabled(False)
            if not self.question_display.isReadOnly():
                self.question_display.setReadOnly(
                    True
                )  # Make it read-only again after fetching the question
            self.answer_display.clear()
            system_prompt = self.config["system_prompt"]
            temperature = self.config["temperature"]
            history = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ]
            self.chat_thread = ChatThread(self.client, history, temperature)
            self.chat_thread.new_message_signal.connect(self.update_answer_display)
            self.chat_thread.finished.connect(
                self.reset_generate_button
            )  # Reset button when done
            self.chat_thread.start()

    def update_button_text(self):
        self.dot_count = (self.dot_count % 3) + 1
        self.generate_answer_btn.setText(f"Generating{'.' * self.dot_count}")

    def reset_generate_button(self):
        self.generate_answer_btn.setText("Generate Answer")
        self.timer.stop()
        # Re-enable UI components
        self.question_list.setEnabled(True)
        self.pass_btn.setEnabled(True)
        self.fail_btn.setEnabled(True)
        self.generate_answer_btn.setEnabled(True)
        self.reload_api_btn.setEnabled(True)
        self.custom_question_btn.setEnabled(True)

    def update_answer_display(self, message):
        self.answer_display.moveCursor(QTextCursor.End)
        self.answer_display.insertPlainText(message)

    def stop_answer_generation(self):
        if hasattr(self, "chat_thread") and self.chat_thread.isRunning():
            self.chat_thread.terminate()
            self.chat_thread.wait()
            del self.chat_thread

    def remove_widget_from_layout(self, widget):
        widget.hide()
        self.qa_layout.removeWidget(widget)
        widget.deleteLater()

    def enable_custom_question(self):
        self.stop_answer_generation()
        self.question_display.setReadOnly(False)
        self.question_display.clear()
        self.answer_display.clear()

    def reload_api_connection(self):
        try:
            self.client = initialize_client(
                self.config["base_url"], self.config["api_key"]
            )
            self.model_name = get_model_name(self.client)
        except Exception as e:
            self.model_name = "Model Offline / Connectivity Error"
        self.model_label.setText(
            f"Model: {self.model_name}"
            if self.model_name
            else "Model Offline / Connectivity Error - Check Your LLM and Config values and make sure they're correct"
        )

    def mark_as_pass(self):
        current_item = self.question_list.currentItem()
        current_row = self.question_list.currentRow()
        if current_item:
            current_item.setBackground(QColor("#98FB98"))
            current_item.setForeground(
                QBrush(QColor("black"))
            )  # Set text color to black
            self.graded_questions.add(current_row)  # Add to graded questions
            self.reset_test_btn.setEnabled(True)  # Enable Reset Test button
        print("Answer marked as Pass")
        self.moveToNextQuestion()

    def mark_as_fail(self):
        current_item = self.question_list.currentItem()
        current_row = self.question_list.currentRow()
        if current_item:
            current_item.setBackground(QColor("#FFB6C1"))
            current_item.setForeground(
                QBrush(QColor("black"))
            )  # Set text color to black
            self.graded_questions.add(current_row)  # Add to graded questions
            self.reset_test_btn.setEnabled(True)  # Enable Reset Test button
        print("Answer marked as Fail")
        self.moveToNextQuestion()

    def moveToNextQuestion(self):
        current_row = self.question_list.currentRow()
        next_row = (
            current_row + 1 if current_row + 1 < self.question_list.count() else 0
        )
        found_ungraded = False

        # Loop through the list starting from the next row, wrapping around if necessary
        for _ in range(self.question_list.count()):
            if next_row not in self.graded_questions:
                found_ungraded = True
                break
            next_row = (next_row + 1) % self.question_list.count()

        if found_ungraded:
            self.question_list.setCurrentRow(next_row)
        else:
            # If all questions have been graded, show a summary popup
            correct_answers = len(
                [
                    row
                    for row in range(self.question_list.count())
                    if self.question_list.item(row).background().color()
                    == QColor("#98FB98")
                ]
            )
            total_questions = self.question_list.count()
            score_percent = (correct_answers / total_questions) * 100
            QMessageBox.information(
                self,
                "Grading Complete",
                f"Correctly Answered: {correct_answers}/{total_questions}\nScore: {score_percent:.2f}%",
            )

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.generate_answer()
        # j key moves to next item in list, k key moves to previous list item, vim style
        elif event.key() == Qt.Key_J:
            # move to next index
            self.question_list.setCurrentRow((self.question_list.currentRow() + 1) % self.question_list.count())
        elif event.key() == Qt.Key_K:
            # move to previous index
            self.question_list.setCurrentRow((self.question_list.currentRow() - 1) % self.question_list.count())
        else:
            super().keyPressEvent(event)

    

    def reset_test(self):
        for row in range(self.question_list.count()):
            item = self.question_list.item(row)
            item.setBackground(QBrush())  # Clear background color to default
            item.setForeground(QBrush())  # Clear text color to default
        self.graded_questions.clear()  # Clear graded questions set
        self.reset_test_btn.setEnabled(False)  # Disable Reset Test button
