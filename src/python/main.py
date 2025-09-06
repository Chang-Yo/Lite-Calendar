import sys
from PySide6.QtWidgets import QApplication
from app.main_window import MainWindow
from app.database import init_database

def main():
    # Ensure the database is ready every time the app starts
    init_database()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
