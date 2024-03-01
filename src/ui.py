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
    """
    Initialize the user interface with buttons, displays, and layouts.
    
    Args:
    main_window: The main window object to initialize the UI on.
    """
    # Create the main layout
    main_layout = QHBoxLayout()

    # Create the left vertical layout
    left_vlayout = QVBoxLayout()

    # Add Reload API Connection button
    main_window.reload_api_btn = QPushButton("Reload API Connection")
    main_window.reload_api_btn.clicked.connect(main_window.reload_api_connection)
    left_vlayout.addWidget(main_window.reload_api_btn)

    # Add Custom Question button
    main_window.custom_question_btn = QPushButton("Custom Question")
    main_window.custom_question_btn.clicked.connect(main_window.enable_custom_question)
    left_vlayout.addWidget(main_window.custom_question_btn)

    # Add Reset Test button
    main_window.reset_test_btn = QPushButton("Reset Test")
    main_window.reset_test_btn.clicked.connect(main_window.reset_test)
    main_window.reset_test_btn.setEnabled(False)  # Disabled by default
    left_vlayout.addWidget(main_window.reset_test_btn)

    # Create and configure the question list widget
    main_window.question_list = QListWidget()
    main_window.question_list.currentItemChanged.connect(main_window.display_question_from_list)
    main_window.question_list.setWordWrap(True)
    main_window.question_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    left_vlayout.addWidget(main_window.question_list, 1)

    # Infobox widget with Patreon, YouTube, Twitter, Discord GitHub, and 2 images (my avatar + Obsidian logo)
    main_window.infobox = QWidget()
    main_window.infobox_layout = QHBoxLayout()
    main_window.infobox.setLayout(main_window.infobox_layout)

    # Populate the question list
    for question in main_window.questions:
        question_preview = question[:40] + "..." if len(question) > 40 else question
        item = QListWidgetItem(question_preview)
        item.setData(Qt.UserRole, question)
        main_window.question_list.addItem(item)

    # Add the left vertical layout to the main layout
    main_layout.addLayout(left_vlayout, 1)

    # Create the QA vertical layout and top horizontal layout
    main_window.qa_layout = QVBoxLayout()
    main_window.top_hlayout = QHBoxLayout()

    # Add the model label to the top horizontal layout
    main_window.model_label = QLabel(
        f"Model: {main_window.model_name}"
        if main_window.model_name
        else "No Model Loaded"
    )
    main_window.top_hlayout.addWidget(main_window.model_label)
    main_window.qa_layout.addLayout(main_window.top_hlayout)

    # Add question and answer displays to the QA layout
    main_window.question_display = QTextEdit()
    main_window.question_display.setReadOnly(True)
    main_window.qa_layout.addWidget(main_window.question_display)

    main_window.answer_display = QTextEdit()
    main_window.answer_display.setReadOnly(True)
    main_window.qa_layout.addWidget(main_window.answer_display)

    # Add the Generate Answer button to the QA layout
    main_window.generate_answer_btn = QPushButton("Generate Answer")
    main_window.generate_answer_btn.clicked.connect(main_window.generate_answer)
    main_window.qa_layout.addWidget(main_window.generate_answer_btn)

    # Add Pass and Fail buttons to the QA layout
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

    # Add the QA layout to the main layout
    main_layout.addLayout(main_window.qa_layout, 3)

    # Create the central widget and set the layout
    central_widget = QWidget()
    central_widget.setLayout(main_layout)
    main_window.setCentralWidget(central_widget)
