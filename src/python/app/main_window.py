from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QCalendarWidget, QListWidget, QListWidgetItem, QPushButton)
from PySide6.QtCore import QDate
from .database import get_events_by_date, add_event, delete_event
from .add_event_dialog import AddEventDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lite-Calendar")
        self.resize(500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        main_layout.addWidget(self.calendar)

        button_layout = QHBoxLayout()
        self.add_event_button = QPushButton("Add Event")
        self.add_event_button.clicked.connect(self.open_add_event_dialog)
        self.delete_event_button = QPushButton("Delete Event")
        self.delete_event_button.clicked.connect(self.delete_selected_event)
        self.delete_event_button.setEnabled(False) # Initially disabled
        button_layout.addWidget(self.add_event_button)
        button_layout.addWidget(self.delete_event_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        self.events_list = QListWidget()
        self.events_list.itemSelectionChanged.connect(self.update_delete_button_state)
        main_layout.addWidget(self.events_list)

        self.calendar.selectionChanged.connect(self.update_events_list)
        self.update_events_list()

    def open_add_event_dialog(self):
        dialog = AddEventDialog(self)
        if dialog.exec():
            details = dialog.get_details()
            if details and details['title']:
                selected_date = self.calendar.selectedDate().toString("yyyy-MM-dd")
                add_event(date=selected_date, time=details['time'], title=details['title'], description=details['description'])
                self.update_events_list()

    def delete_selected_event(self):
        selected_items = self.events_list.selectedItems()
        if not selected_items: return

        # The event ID is stored in the item's data
        event_id = selected_items[0].data(QDate.UserRole)
        if event_id:
            delete_event(event_id)
            self.update_events_list()

    def update_events_list(self):
        self.events_list.clear()
        selected_date = self.calendar.selectedDate()
        date_str = selected_date.toString("yyyy-MM-dd")
        events = get_events_by_date(date_str)
        
        if not events:
            self.events_list.addItem("No events for this day.")
            self.events_list.setEnabled(False)
        else:
            self.events_list.setEnabled(True)
            for event in events:
                list_item_text = f"{event['time']}: {event['title']}"
                list_item = QListWidgetItem(list_item_text)
                # Store the database ID in the item itself
                list_item.setData(QDate.UserRole, event['id'])
                self.events_list.addItem(list_item)
        self.update_delete_button_state()

    def update_delete_button_state(self):
        # Enable the delete button only if an item is selected
        self.delete_event_button.setEnabled(len(self.events_list.selectedItems()) > 0)
