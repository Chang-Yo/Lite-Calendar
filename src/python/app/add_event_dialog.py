from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
    QTextEdit, QDialogButtonBox, QTimeEdit
)
from PySide6.QtCore import QTime

class AddEventDialog(QDialog):
    """A dialog window for adding or editing an event."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Add New Event")

        self.layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        self.time_edit = QTimeEdit()
        self.time_edit.setDisplayFormat("HH:mm")
        self.time_edit.setTime(QTime.currentTime())
        form_layout.addRow("Time:", self.time_edit)

        self.title_edit = QLineEdit()
        form_layout.addRow("Title:", self.title_edit)

        self.description_edit = QTextEdit()
        form_layout.addRow("Description:", self.description_edit)

        self.layout.addLayout(form_layout)

        # Standard OK and Cancel buttons
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.button_box)

    def get_details(self):
        """Returns the entered event details as a dictionary."""
        if self.result() == QDialog.Accepted:
            return {
                "time": self.time_edit.time().toString("HH:mm"),
                "title": self.title_edit.text(),
                "description": self.description_edit.toPlainText()
            }
        return None
