from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QTextEdit,
    QWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor, QBrush


def initUI(main_window):
    main_layout = QHBoxLayout()

    left_vlayout = QVBoxLayout()

    main_window.reload_api_btn = QPushButton("Reload API Connection")
    main_window.reload_api_btn.clicked.connect(main_window.reload_api_connection)
    left_vlayout.addWidget(main_window.reload_api_btn)

    main_window.custom_question_btn = QPushButton("Custom Question")
    main_window.custom_question_btn.clicked.connect(main_window.enable_custom_question)
    left_vlayout.addWidget(main_window.custom_question_btn)

    main_window.question_list = QListWidget()
    main_window.question_list.currentItemChanged.connect(
        main_window.display_question_from_list
    )
    main_window.question_list.setWordWrap(True)
    main_window.question_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    left_vlayout.addWidget(main_window.question_list, 1)

    for question in main_window.questions:
        question_preview = question[:40] + "..." if len(question) > 40 else question
        item = QListWidgetItem(question_preview)
        item.setData(Qt.UserRole, question)
        main_window.question_list.addItem(item)

    main_layout.addLayout(left_vlayout, 1)

    main_window.qa_layout = QVBoxLayout()
    main_window.top_hlayout = QHBoxLayout()
    main_window.model_label = QLabel(
        f"Model: {main_window.model_name}"
        if main_window.model_name
        else "No Model Loaded"
    )
    main_window.top_hlayout.addWidget(main_window.model_label)
    main_window.qa_layout.addLayout(main_window.top_hlayout)

    main_window.question_display = QTextEdit()
    main_window.question_display.setReadOnly(True)
    main_window.qa_layout.addWidget(main_window.question_display)

    main_window.answer_display = QTextEdit()
    main_window.answer_display.setReadOnly(True)
    main_window.qa_layout.addWidget(main_window.answer_display)

    main_window.generate_answer_btn = QPushButton("Generate Answer")
    main_window.generate_answer_btn.clicked.connect(main_window.generate_answer)
    main_window.qa_layout.addWidget(main_window.generate_answer_btn)

    buttons_hlayout = QHBoxLayout()

    main_window.pass_btn = QPushButton("Pass")
    main_window.pass_btn.setStyleSheet("background-color: #98FB98; color: black;")
    main_window.pass_btn.clicked.connect(main_window.mark_as_pass)
    buttons_hlayout.addWidget(main_window.pass_btn)

    main_window.fail_btn = QPushButton("Fail")
    main_window.fail_btn.setStyleSheet("background-color: #FFB6C1; color: black;")
    main_window.fail_btn.clicked.connect(main_window.mark_as_fail)
    buttons_hlayout.addWidget(main_window.fail_btn)

    main_window.qa_layout.addLayout(buttons_hlayout)

    main_layout.addLayout(main_window.qa_layout, 3)

    central_widget = QWidget()
    central_widget.setLayout(main_layout)
    main_window.setCentralWidget(central_widget)
