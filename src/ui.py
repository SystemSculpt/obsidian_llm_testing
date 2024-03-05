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
from PySide6.QtGui import (
    QFont,
    QColor,
    QBrush,
    QPixmap,
    QPainter,
    QPen,
    QIcon,
    QImage,
    QRegion,
    QBitmap,
)


def create_circular_avatar(image_path, size=150):
    # Load the image
    pixmap = QPixmap(image_path)
    # Resize the image to the specified size
    pixmap = pixmap.scaled(size, size, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    # Create a new QPixmap to draw the circular mask
    circle_pixmap = QPixmap(size, size)
    circle_pixmap.fill(Qt.transparent)  # Fill with transparent background

    # Create a QPainter to draw the circular mask
    painter = QPainter(circle_pixmap)
    painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smooth edges
    painter.setBrush(
        QBrush(pixmap)
    )  # Use the original pixmap as the brush to retain the image
    painter.setPen(QPen(Qt.NoPen))  # No border

    # Draw a circle
    painter.drawEllipse(0, 0, size, size)

    # End painting
    painter.end()

    return circle_pixmap


def initUI(main_window):
    """
    Initialize the user interface with buttons, displays, and layouts.

    Args:
    main_window: The main window object to initialize the UI on.
    """
    # Create the main layout
    main_layout = QHBoxLayout()
    margin = 35
    main_layout.setContentsMargins(margin, margin, margin, margin)  # Set the margins

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
    main_window.question_list.currentItemChanged.connect(
        main_window.display_question_from_list
    )
    main_window.question_list.setWordWrap(True)
    main_window.question_list.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    # Populate the question list
    for question in main_window.questions:
        question_preview = question[:40] + "..." if len(question) > 40 else question
        item = QListWidgetItem(question_preview)
        item.setData(Qt.UserRole, question)
        main_window.question_list.addItem(item)
    left_vlayout.addWidget(main_window.question_list)

    # Infobox widget with Patreon, YouTube, GitHub, and 2 images (Obsidian logo + SystemSculpt logo)
    main_window.infobox = QWidget()
    infobox_layout = QVBoxLayout()  # Adjust layout as needed
    main_window.infobox.setLayout(infobox_layout)

    # Horizontal layout for logos
    logos_hlayout = QHBoxLayout()

    # Add icons with circular cutout
    obsidian_icon = QLabel()
    obsidian_pixmap = create_circular_avatar("img/obsidian_logo.jpg")
    obsidian_icon.setPixmap(obsidian_pixmap)
    logos_hlayout.addWidget(obsidian_icon)

    systemsculpt_icon = QLabel()
    systemsculpt_pixmap = create_circular_avatar("img/systemsculpt_logo.jpg")
    systemsculpt_icon.setPixmap(systemsculpt_pixmap)
    logos_hlayout.addWidget(systemsculpt_icon)

    # Center the logos horizontally
    logos_hlayout.setAlignment(Qt.AlignCenter)

    # Add the logos layout to the infobox layout
    infobox_layout.addLayout(logos_hlayout)

    # Horizontal layout for Patreon link
    patreon_hlayout = QHBoxLayout()
    patreon_label = QLabel('<a href="https://patreon.com/systemsculpt">Patreon</a>')
    patreon_label.setOpenExternalLinks(True)
    patreon_hlayout.addWidget(patreon_label, 0, Qt.AlignCenter)  # Center the label
    infobox_layout.addLayout(patreon_hlayout)  # Add the layout to the infobox layout

    # Horizontal layout for YouTube link
    youtube_hlayout = QHBoxLayout()
    youtube_label = QLabel('<a href="https://youtube.com/@systemsculpt">YouTube</a>')
    youtube_label.setOpenExternalLinks(True)
    youtube_hlayout.addWidget(youtube_label, 0, Qt.AlignCenter)  # Center the label
    infobox_layout.addLayout(youtube_hlayout)  # Add the layout to the infobox layout

    # Horizontal layout for GitHub link
    github_hlayout = QHBoxLayout()
    github_label = QLabel('<a href="https://github.com/systemsculpt">GitHub</a>')
    github_label.setOpenExternalLinks(True)
    github_hlayout.addWidget(github_label, 0, Qt.AlignCenter)  # Center the label
    infobox_layout.addLayout(github_hlayout)  # Add the layout to the infobox layout

    # Add the infobox to the left vertical layout below the question list
    left_vlayout.addWidget(main_window.infobox)

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
    font = main_window.model_label.font()
    font.setPointSize(font.pointSize())
    main_window.model_label.setFont(font)
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
